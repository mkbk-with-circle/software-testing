import json
import re
import argparse

def parse_diff(diff_path):
    with open(diff_path, 'r') as f:
        lines = f.readlines()

    patches = []
    current_file = None
    i = 0

    while i < len(lines):
        line = lines[i]
        # 更新当前文件（提取文件名部分）
        if line.startswith('+++'):
            parts = line.strip().split()
            if len(parts) >= 2:
                current_file = parts[1]
                # 如果路径前缀是 "test/patch/", 移除之
                prefix = "test/patch/"
                if current_file.startswith(prefix):
                    current_file = current_file[len(prefix):]
            i += 1
            continue
        # 解析 hunk 开始
        elif line.startswith('@@'):
            m = re.match(r'@@ -(\d+)(?:,\d*)? \+(\d+)(?:,\d*)? @@', line)
            if not m:
                i += 1
                continue

            old_line = int(m.group(1))
            new_line = int(m.group(2))
            cur_old = old_line
            cur_new = new_line
            i += 1

            # 在当前 hunk 内分割出多个连续变更块
            current_block = None
            while i < len(lines) and not lines[i].startswith('@@') and not lines[i].startswith('diff') and not lines[i].startswith('+++'):
                curr_line = lines[i]
                if curr_line.startswith(' '):
                    # 遇到上下文行，若有正在收集的块则结束该块
                    if current_block is not None:
                        patches.append(build_patch(current_file, current_block))
                        current_block = None
                    cur_old += 1
                    cur_new += 1
                    i += 1
                elif curr_line.startswith('-') and not curr_line.startswith('---'):
                    if current_block is None:
                        current_block = {
                            'deleted_lines': [],
                            'inserted_lines': [],
                            'start_old': cur_old,
                            'start_new': cur_new,
                            'end_old': cur_old
                        }
                    current_block['deleted_lines'].append(curr_line[1:])
                    current_block['end_old'] = cur_old
                    cur_old += 1
                    i += 1
                elif curr_line.startswith('+') and not curr_line.startswith('+++'):
                    if current_block is None:
                        current_block = {
                            'deleted_lines': [],
                            'inserted_lines': [],
                            'start_old': cur_old,  # 使用原始文件的当前行号
                            'start_new': cur_new,
                            'end_old': cur_old
                        }
                    current_block['inserted_lines'].append(curr_line[1:])
                    # 注意：插入行不影响原始文件行号
                    cur_new += 1
                    i += 1
                else:
                    i += 1
            # hunk结束后，如果还有未提交的块，则添加
            if current_block is not None:
                patches.append(build_patch(current_file, current_block))
        else:
            i += 1

    result = {"num_of_hunks": len(patches)}
    for idx, patch in enumerate(patches):
        result[str(idx)] = patch
    return result

def build_patch(current_file, block):
    """
    根据一个连续变更块构造 patch 字典：
      - 只有插入行 => insert patch，next_line_no 用 block['start_old']
      - 只有删除行 => delete patch
      - 同时有删除和插入 => replace patch
    """
    patch = {"file_name": current_file}
    if block['inserted_lines'] and not block['deleted_lines']:
        patch['patch_type'] = 'insert'
        patch['replaced_with'] = ''.join(block['inserted_lines'])
        patch['next_line_no'] = block['start_old']  # 使用原始文件行号
    elif block['deleted_lines'] and not block['inserted_lines']:
        patch['patch_type'] = 'delete'
        patch['replaced'] = ''.join(block['deleted_lines'])
        patch['from_line_no'] = block['start_old']
        patch['to_line_no'] = block['end_old']
        patch['next_line_no'] = block['end_old'] + 1
    elif block['deleted_lines'] and block['inserted_lines']:
        patch['patch_type'] = 'replace'
        patch['replaced'] = ''.join(block['deleted_lines'])
        patch['replaced_with'] = ''.join(block['inserted_lines'])
        patch['from_line_no'] = block['start_old']
        patch['to_line_no'] = block['end_old']
        patch['next_line_no'] = block['end_old'] + 1
    return patch

if __name__ == "__main__":
    parser =  argparse.ArgumentParser(description="devert patch to json")
    parser.add_argument('project', help='Defects4J project name, e.g. Lang')
    parser.add_argument('bug_id', help='Bug identifier, integer')
    args = parser.parse_args()
    project = args.project
    bug_id = args.bug_id
    file_parse = "../../..//patch.diff"
    output = parse_diff(file_parse)
    output_file = f"../../../an-implementation-of-chatrepair/patches/{project}/{bug_id}.json"
    print("output_file", output_file)
    with open(output_file, "w") as f:
        json.dump(output, f, indent=4)
