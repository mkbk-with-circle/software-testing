import json
import os
import re
import difflib
import sys
import time

import openai
import subprocess
from javalang import parse
from javalang.tree import MethodDeclaration
from constants import *
  
previous_failure_test = ''
project_name = ""
project_num = ""


def save_initial(project, all_single_function_flag):
    # 获取项目目录下的所有文件
    files = os.listdir(os.path.join(PATCH_JSON_FOLDER, project))
    # 排序
    files.sort(key=lambda x: int(x.rstrip('.json')))
    for file in files:
        global project_num
        project_num = file.rstrip('.json')
        initial_prompt = ''
        # 根据标志选择构建单函数或完整初始提示
        print("now json file is:",file)
        if all_single_function_flag == True:
            initial_prompt = construct_single_function_initial_prompt(project, file)
        else:
            initial_prompt = construct_initial_prompt(project, file)
        # 如果初始提示不为空，保存到文件
        if not initial_prompt == '':
            f = open_file(os.path.join(INITIAL_PROMPT_FOLDER, project, file.rstrip(".json") + ".txt"), 'w')
            f.write(initial_prompt)
    # 打印成功信息
    print("Success!\nInitial Prompt is saved in " + INITIAL_PROMPT_FOLDER + "/" + project + "!")


def chat_initial(project, all_single_function_flag):
    openai.base_url = BASE_URL
    openai.api_key = API_KEY
    json_files = os.listdir(os.path.join(PATCH_JSON_FOLDER, project))
    for json_file in json_files:
        i = 0
        no = json_file.rstrip('.json')
        while i < NUMOFREPEAT_PER_BUG:
            initial_prompt = ''
            if all_single_function_flag == True:
                initial_prompt = construct_single_function_initial_prompt(project, json_file)
            else:
                initial_prompt = construct_initial_prompt(project, json_file)
            if not initial_prompt == '':
                context = [{'role': 'user', 'content': initial_prompt}]
                response = openai.chat.completions.create(model=MODEL, messages=context)
                # The program pauses for 1 second to prevent excessive request frequency.
                time.sleep(1)
                response_text = response.choices[0].message.content
                context.append({'role': 'assistant', 'content': response_text})
                patch = match_patch_code(response_text)
                # If no valid patch is found, restart the cycle.
                if patch == '':
                    continue
                result = []
                feedback = validate_patch(patch, project, json_file, all_single_function_flag, result)
                if feedback == 'Exception':
                    continue
                
                # Save the conversation to their respective files.
                context_path = os.path.join(INITIALCHAT_FOLDER, project, 'bug' + no, str(i+1) + '.txt')
                file = open_file(context_path, 'w')
                for element in context:
                    file.write(element['content'])
                    file.write('\n\n')
                if all_single_function_flag:
                    # Get the diff result of the patch and the buggy function.
                    diff_result = diff_buggy_and_new(project, json_file, patch)
                    file.write(diff_result)
                file.close()
                i += 1
            else:
                break
            # Save data to the summary file.
            file = open_file(os.path.join(INITIALCHAT_FOLDER, INITIALCHAT_STATISTIFCS_FILE), 'a')
            file.write(project + ', ' + no + ', ' + PATCH_FAILURE_CATEGORY[result[0]] + '\n')
            file.close()


def diff_buggy_and_new(project, json_file, new_function):
    no = json_file.rstrip('.json')
    with open(os.path.join(PATCH_JSON_FOLDER, project, json_file), 'r', encoding="latin-1") as f:
        data = json.load(f)
        f.close()
    if not os.path.exists(os.path.join(BUGGY_PROJECT_FOLDER, project + no)):
        os.system(DEFECTS4J_CHECKOUT % (project, no + 'b', os.path.join(BUGGY_PROJECT_FOLDER, project + no)))
    next_line_no = data['0']['next_line_no']
    file_name = data['0']['file_name']
    source_file_path = os.path.join(BUGGY_PROJECT_FOLDER, project + no, file_name)
    buggy_function = get_buggy_function(source_file_path, next_line_no, next_line_no, PATCH_TYPE_DELETE)
    diff = difflib.Differ()
    buggy_squences = [line.strip() for line in buggy_function.splitlines() if line.strip()]
    new_squences = [line.strip() for line in new_function.splitlines() if line.strip()]
    return '\n'.join(diff.compare(buggy_squences, new_squences))


def diff_buggy_and_newlist(project, json_file, new_function_list):
    no = json_file.rstrip('.json')
    with open(os.path.join(PATCH_JSON_FOLDER, project, json_file), 'r', encoding="latin-1") as f:
        data = json.load(f)
        f.close()
    if not os.path.exists(os.path.join(BUGGY_PROJECT_FOLDER, project + no)):
        os.system(DEFECTS4J_CHECKOUT % (project, no + 'b', os.path.join(BUGGY_PROJECT_FOLDER, project + no)))
    next_line_no = data['0']['next_line_no']
    file_name = data['0']['file_name']
    source_file_path = os.path.join(BUGGY_PROJECT_FOLDER, project + no, file_name)
    buggy_function = get_buggy_function(source_file_path, next_line_no, next_line_no, PATCH_TYPE_DELETE)
    diff = difflib.Differ()
    buggy_squences = [line.strip() for line in buggy_function.splitlines() if line.strip()]
    diff_result = []
    for new_function in new_function_list:
        new_squences = [line.strip() for line in new_function.splitlines() if line.strip()]
        diff_result.append('\n'.join(diff.compare(buggy_squences, new_squences)))
    return diff_result


def go_chat_repair(project, all_single_function_flag):
    openai.base_url = BASE_URL
    openai.api_key = API_KEY
    files = os.listdir(os.path.join(PATCH_JSON_FOLDER, project))
    i = 0
    while i < len(files):
        initial_prompt = ''
        if all_single_function_flag == True:
            initial_prompt = construct_single_function_initial_prompt(project, files[i])
        else:
            initial_prompt = construct_initial_prompt(project, files[i])
        # Skip test files that do not meet the requirements or are not single hunk.
        if initial_prompt == '':
            i += 1
        if not initial_prompt == '':
            # If chatrepair throws an exception, retry the current bug.
            if chat_repair(project, initial_prompt, files[i], all_single_function_flag) != 'Exception':
                i += 1


def chat_repair(project, initial_prompt, json_file, all_single_function_flag):
    current_tries = 0
    plausible_patches = []

    openai.base_url = BASE_URL
    openai.api_key = API_KEY
    
    # Track feedback status values.
    fa = 0
    fb = 0
    first_plausible_try = 0
    
    # Find a plausible patch.
    while current_tries < Max_Tries and len(plausible_patches) == 0:
        context = []
        current_length = 0
        prompt = initial_prompt
        # Add feedback list to track feedback effects.
        feedback_list = []
        while current_length < Max_Conv_len:
            context.append({'role': 'user', 'content': prompt})
            response = openai.chat.completions.create(model=MODEL, messages=context)
            # The program pauses for 1 second.
            time.sleep(1)
            response_text = response.choices[0].message.content
            context.append({'role': 'assistant', 'content': response_text})
            patch = match_patch_code(response_text)
            # Skip this conversation if the response does not conform to the standard.
            if patch == '':
                break
            feedback = validate_patch(patch, project, json_file, all_single_function_flag, feedback_list)
            if feedback == '':
                plausible_patches.append(patch)
                current_length += 1
                current_tries += 1
                break
            if feedback == 'Exception':
                return 'Exception'
            else:
                prompt = feedback
            current_length += 1
            current_tries += 1
            
        # Process feedback_list: validate is called 3 times if not fixed, or 1, 2, or 3 times if fixed.
        a, b = process_fb_list(feedback_list)
        fa += a
        fb += b
        # Save results to respective files.
        file = open_file(os.path.join(CHATREPAIR_FOLDER, project, json_file.rstrip('.json') + '.txt'), 'a')
        file.write('current trys: ' + str(current_tries) + ', feedback list: ' + str(feedback_list) + ' Feedback statistics: ' + str(fa) + '/' + str(fb) + '\n')
        if feedback_list[len(feedback_list)-1] == 5:
            first_plausible_try = current_tries
            file.write('current trys: ' + str(current_tries) + ', feedback list: ' + str(feedback_list) + ' First plausible patch at ' + str(current_tries) + ' tries!\n')
        file.close()
        
        # Save conversation to respective files.
        context_path = os.path.join(CHATREPAIR_FOLDER, project, 'bug' + json_file.rstrip('.json'),
                                    str(current_tries) + '.txt')
        file = open_file(context_path, 'w')
        for element in context:
            file.write(element['content'])
            file.write('\n\n')
        file.close()
        
    # Save results to the summary file.
    file = open_file(os.path.join(CHATREPAIR_FOLDER, FEEDBACK_STATISTICS_FILE), 'a')
    file.write(project + ', ' + json_file.rstrip('.json') + ', ' + str(fa) + ', ' + str(fb) + ', ' + str(first_plausible_try) + '\n')
    file.close()
        
    # If a plausible patch is found, generate more plausible patches.
    if len(plausible_patches) != 0:
        alternatives_list = []
        duplicates_num = 0
        while current_tries < Max_Tries:
            context = []
            patches_prompt = ''
            patch_or_function = 'plausible patch '
            if all_single_function_flag:
                patch_or_function = 'Correct version '
            for i in range(len(plausible_patches)):
                patches_prompt += patch_or_function + str(i+1) + ' :\n' + plausible_patches[i] + '\n'
            if all_single_function_flag:
                prompt = delete_substring_to_end(initial_prompt.split('<Example end>')[1].strip(), "Please provide") + Alt_Instruct_3 + patches_prompt + Alt_Instruct_4
            else: 
                prompt = delete_substring_to_end(initial_prompt.split('<Example end>')[1].strip(), "Please provide") + Alt_Instruct_1 + patches_prompt + Alt_Instruct_2
            context.append({'role': 'user', 'content': prompt})
            response = openai.chat.completions.create(model=MODEL, messages=context)
            # The program pauses for 1 second.
            time.sleep(1)
            response_text = response.choices[0].message.content
            context.append({'role': 'assistant', 'content': response_text})
            patch = match_patch_code(response_text)
            # Skip this conversation if the response does not conform to the standard.
            if patch == '':
                continue
            feedback = validate_patch(patch, project, json_file, all_single_function_flag, alternatives_list)
            if feedback == 'Exception':
                return 'Exception'
            # Check if the specified string is already present.
            if feedback == '':
                if not_exist(plausible_patches, patch):
                    plausible_patches.append(patch)
                else:
                    duplicates_num += 1
            current_tries += 1
            # Save conversation to respective files.
            context_path = os.path.join(CHATREPAIR_FOLDER, project, 'bug' + json_file.rstrip('.json'),
                                        str(current_tries) + '.txt')
            file = open_file(context_path, 'w')
            for element in context:
                file.write(element['content'])
                file.write('\n')
            file.close()
        
        # Get patch statistics        
        num_ce_patches, num_f_patches, num_to_patches, num_plausible_patches = proces_alter_list(alternatives_list)
        # Include the first plausible patch
        num_plausible_patches += 1
        # Save results to respective files
        file = open_file(os.path.join(CHATREPAIR_FOLDER, project, json_file.rstrip('.json')) + '.txt', 'a')
        file.write('current trys: ' + str(current_tries) + '. Below is statistics of all generation patches:\n')
        file.write('\nCompilation Error patches number: ' + str(num_ce_patches) + '\nFailure patches number: '
                + str(num_f_patches) + '\nTime out patches number: ' + str(num_to_patches) + '\nPlausible patches number: '
                + str(num_plausible_patches) + '\nDuplicate plausible patches number: ' + str(duplicates_num))
        file.close()
        # Save results to summary file
        file = open_file(os.path.join(CHATREPAIR_FOLDER, ALTERNATIVES_STATISTICS_FILE), 'a')
        file.write(project + ', ' + json_file.rstrip('.json') + ', ' + str(num_ce_patches) + ', ' + str(num_f_patches) + ', '
                + str(num_to_patches) + ', ' + str(num_plausible_patches) + ', ' + str(duplicates_num) + ', ' + str(len(plausible_patches)) + '\n')
        file.close()
        # Save diff results to respective files
        file = open_file(os.path.join(CHATREPAIR_FOLDER, project, 'bug' + json_file.rstrip('.json'), 'diffpatches.txt'), 'w')
        diff_result = diff_buggy_and_newlist(project, json_file, plausible_patches)
        for result in diff_result:
            file.write(result + '\n\n')
        file.close()
    return plausible_patches


# Validate the corresponding patch and construct feedback
def validate_patch(patch, project, json_file, all_single_function_flag, fb_list):
    global previous_failure_test
    temp_javafile = ''
    javafile_path = ''
    no = json_file.rstrip('.json')
    # If the folder for the corresponding bug does not exist, run defects4j checkout
    if not os.path.exists(os.path.join(BUGGY_PROJECT_FOLDER, project + no)):
        os.system(DEFECTS4J_CHECKOUT % (
            project, no + 'b', os.path.join(BUGGY_PROJECT_FOLDER, project + no)))
    with open(os.path.join(PATCH_JSON_FOLDER, project, json_file), 'r', encoding="latin-1") as f:
        data = json.load(f)
        f.close()
    # Flags for single line and single function patches
    single_line = False
    single_function = False 
    file_name = data['0']['file_name']
    patch_type = data['0']['patch_type']
    javafile_path = os.path.join(BUGGY_PROJECT_FOLDER, project + no, file_name)
    
    # Backup the file to be modified, restore it after verification
    with open(javafile_path, mode='r', encoding='latin-1') as javafile:
        temp_javafile = javafile.read()
        javafile.close
    if all_single_function_flag == False:  
        # For replace-type patches, find the corresponding source code file and replace the specified lines with the patch
        if patch_type == PATCH_TYPE_REPLACE:
            from_line_no = data['0']['from_line_no']
            to_line_no = data['0']['to_line_no']
            if from_line_no == to_line_no:
                single_line = True
            # Read the java file
            with open(javafile_path, mode='r', encoding='latin-1') as f1:
                lines = f1.readlines()
            del lines[from_line_no - 1:to_line_no]
            lines.insert(from_line_no - 1, patch)
            f1.close()
            # After modification, write the new lines back into the java file
            with open(javafile_path, mode='w', encoding='latin-1') as f2:
                f2.writelines(lines)
            f2.close()
        # For insert-type patches
        if patch_type == PATCH_TYPE_INSERT:
            next_line_no = data['0']['next_line_no']
            with open(javafile_path, mode='r', encoding='latin-1') as f1:
                lines = f1.readlines()
            lines.insert(next_line_no - 1, patch)
            f1.close()
            with open(javafile_path, mode='w', encoding='latin-1') as f2:
                f2.writelines(lines)
                f2.close()
                #print(''.join(lines))
        # For delete-type patches, replace the entire function
        if patch_type == PATCH_TYPE_DELETE:
            single_function = True
            next_line_no = data['0']['next_line_no']
            rewrite_function_to_javafile(next_line_no, javafile_path, patch)
    if all_single_function_flag == True:
        next_line_no = data['0']['next_line_no']
        rewrite_function_to_javafile(next_line_no, javafile_path, patch)
    # Execute defects4j compile; defects4j test and return feedback
    feedback = construct_feedback_after_validate(project, no, fb_list)
    # If feedback is an empty string, the patch is correct
    if feedback == '':
        # After compiling and testing, restore the original content of the java file
        with open(javafile_path, mode='w', encoding='latin-1') as javafile:
            javafile.write(temp_javafile)
            javafile.close()
        return ''
    if feedback == 'Exception':
        # After compiling and testing, restore the original content of the java file
        with open(javafile_path, mode='w', encoding='latin-1') as javafile:
            javafile.write(temp_javafile)
            javafile.close()
        return feedback
    # After compiling and testing, restore the original content of the java file
    with open(javafile_path, mode='w', encoding='latin-1') as javafile:
        javafile.write(temp_javafile)
        javafile.close()
    if single_line:
        feedback += INITIAL_Single_line_final
    if single_function or all_single_function_flag:
        feedback += INITIAL_Single_function_final
    if all_single_function_flag == False and not single_line and not single_function:
        feedback += INITIAL_Single_hunk_final
    return feedback

def rewrite_function_to_javafile(next_line_no, javafile_path, patch):
    # Get the line number where the function declaration is located
    start_line = get_method_declaration_line_no(javafile_path, next_line_no)
    # Replace the entire function
    with open(javafile_path, "r", encoding='latin-1') as file:
        lines = file.readlines()
        file.close()
    left_open_brackets = 0
    right_open_brackets = 0
    end_line = start_line - 1
    for line in lines[start_line - 1:-1]:
        left_open_brackets += line.count('{')
        right_open_brackets += line.count('}')
        end_line += 1
        if left_open_brackets == right_open_brackets and not left_open_brackets == 0:
            break
    del lines[start_line - 1:end_line]
    lines.insert(start_line - 1, patch)
    file.close()
    with open(javafile_path, mode='w', encoding='latin-1') as f2:
        f2.writelines(lines)
    f2.close()


def construct_feedback_after_validate(project, no, fb_list):
    global previous_failure_test
    # Recompile the project
    flag, stdout, stderr = run_command(DEFECTS4J_COMPILE.split(' '), 'latin-1', os.path.join(BUGGY_PROJECT_FOLDER, project + no), TEST_TIMEOUT_MAX_S)
    if not flag:
        print(stderr)    
    pattern = r"BUILD FAILED"
    result = re.search(pattern, stderr, re.DOTALL)
    feedback = ''
    if result:
        errs = stderr.split("\n")
        for i in range(len(errs)):
            if re.search(r":\serror:\s", errs[i]):
                errmsg = 'error' + errs[i].split('error')[1]
                feedback = FeedBack_0 + FeedBack_2 + errmsg
                # Matched compilation errors, add status 2
                fb_list.append(2)
                break
        if feedback == '':
            feedback = FeedBack_0 + FeedBack_3
            # Compilation errors that could not be matched, add status 3
            fb_list.append(3)
    # No compilation errors, run defects4j test
    else:
        temp_failingtests = ''
        failingtests_path = os.path.join(BUGGY_PROJECT_FOLDER, project + no, FAILING_TEST_FILE)
        with open(failingtests_path, mode='r', encoding='latin-1') as failingtests:
            temp_failingtests = failingtests.read()
            failingtests.close()
        flag, stdout, stderr = run_command(DEFECTS4J_TEST.split(' '), 'latin-1', os.path.join(BUGGY_PROJECT_FOLDER, project + no), TEST_TIMEOUT_MAX_S)
        if not flag and stderr.count('[ERROR]') != 0:
            feedback = FeedBack_0 + FeedBack_4
            # Command timeout, add status 4
            fb_list.append(4)
        elif flag:    
            # All tests passed, add plausible_patch
            if is_file_empty_or_not_exists(failingtests_path):   
                # Feedback is empty, end the conversation, add status 5
                fb_list.append(5)
                # Restore the failing_tests file
                with open(failingtests_path, mode='w', encoding='latin-1') as failingtests:
                    failingtests.write(temp_failingtests)
                    failingtests.close()
                return ''
            # If not all tests passed, construct feedback
            failure_test, test_error, test_file, test_line_no = get_failure_test_info(failingtests_path)
            if test_file == '' or test_line_no == '':
                print("Warning!!! Unable to handle file [" + failingtests_path + "]while validate the patch.")
                with open(LOG_FILE, 'a') as file:
                    file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "\nWarning!!! Unable to handle file [" + failingtests_path + "] while validate the patch.")
                    file.close()
                # Restore the failing_tests file
                with open(failingtests_path, mode='w', encoding='latin-1') as failingtests:
                    failingtests.write(temp_failingtests)
                    failingtests.close()
                return 'Exception'
            
            file = os.path.join(BUGGY_PROJECT_FOLDER, project + no, TEST_FILEPATH_PREFIX[project], test_file)
            if not os.path.exists(file):
                file = os.path.join(BUGGY_PROJECT_FOLDER, project + no, TEST_FILEPATH_PREFIX_1, test_file)
            if failure_test == previous_failure_test:
                feedback = FeedBack_0 + FeedBack_1
                # Fail original failure, add status 1
                fb_list.append(1)
            else:
                previous_failure_test = failure_test
                # Fail a new test, add status 0
                fb_list.append(0)
                # Get the test line
                test_lines = []
                with open(file, mode='r', encoding='latin-1') as test_file:
                    lines = test_file.readlines()[test_line_no - 1:]
                    for line in lines:
                        test_lines.append(line)
                        if line.count(';') == 1:
                            break
                feedback = FeedBack_0 + Failure_Test + failure_test + Failure_Test_line + ''.join(
                    test_lines) + Failure_Test_error + test_error
    # Restore the failing_tests file
    with open(failingtests_path, mode='w', encoding='latin-1') as failingtests:
        failingtests.write(temp_failingtests)
        failingtests.close()
    return feedback



def process_fb_list(fb_list):
    a = 0
    # fb_list has 1 to 3 elements
    for i in range(1, len(fb_list)):
        # The current feedback is the same as the previous feedback
        if fb_list[i] == fb_list[i-1]:
            a += 1
    return a, len(fb_list)


def proces_alter_list(alter_list):
    num_ce_patches = 0
    num_f_patches = 0
    num_to_patches = 0
    num_plausible_patches = 0
    
    for alter in alter_list:
        if alter == 0 or alter == 1:
            num_f_patches+=1
        elif alter == 2 or alter == 3:
            num_ce_patches+=1
        elif alter == 4:
            num_to_patches+=1
        elif alter == 5:
            num_plausible_patches+=1
    return num_ce_patches, num_f_patches, num_to_patches, num_plausible_patches


def not_exist(list, s):
    for l in list:
        if l.replace(' ','').replace('\n','') == s.replace(' ','').replace('\n',''):
            return False
    return True
    


# Extract code parts from the ChatGPT response text
def match_patch_code(response_text):
    if(response_text.count('```java') > 1):
        response_text = '\n'.join(response_text.split('\n')[1:])
    pattern = r"```java(.*)```"
    match = re.search(pattern, response_text, re.DOTALL)
    if match is None:
        pattern = r"```(.*)```"
        match = re.search(pattern, response_text, re.DOTALL)
    # Non-standard answer text stops this conversation
    if match is None:
        return ''
    return match.group(1)


# Check if the file exists or is empty
def is_file_empty_or_not_exists(file_path):
    if not os.path.exists(file_path):
        return True
    file_size = os.path.getsize(file_path)
    if file_size == 0:
        return True
    else:
        return False


def delete_substring_to_end(s, subs):
    index = s.find(subs)  # Find the position of the substring in the string
    if index != -1:
        new_string = s[:index]  # Use slicing to get the part before the substring
        return new_string
    else:
        return s


# Run a system command and return standard output and standard error output

def run_command(cmd, encoding='utf-8', cwd=None, timeout=None):
    try:
        finished = subprocess.run(cmd, capture_output=True, cwd=cwd, timeout=timeout)
        finished.check_returncode()
        return True, finished.stdout.decode(encoding), finished.stderr.decode(encoding)
    except subprocess.CalledProcessError:
        return False, finished.stdout.decode(encoding), finished.stderr.decode(encoding)
    except subprocess.TimeoutExpired:
        return False, '[ERROR]:{} time out after {} seconds'.format(cmd, timeout), '[ERROR]:{} time out after {} seconds'.format(cmd, timeout)




# Open a file, create it if it does not exist
def open_file(path, pattern):
    # Check if the path exists
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
    if pattern not in ['r', 'w', 'a']:
        return ''
    file = open(path, pattern)
    return file

# 构建初始提示
def construct_initial_prompt(project, json_file):
    global previous_failure_test
    # 读取对应的 JSON 文件
    no = json_file.rstrip('.json')
    with open(os.path.join(PATCH_JSON_FOLDER, project, json_file), 'r', encoding="latin-1") as f:
        data = json.load(f)
        f.close()
        num_of_hunks = data['num_of_hunks']
        # 如果补丁数量为1，继续处理，因为是初始补丁
        if num_of_hunks == 1:
            # 如果对应的bug文件夹不存在，运行 defects4j checkout
            if not os.path.exists(os.path.join(BUGGY_PROJECT_FOLDER, project + no)):
                os.system(DEFECTS4J_CHECKOUT % (
                    project, no + 'b', os.path.join(BUGGY_PROJECT_FOLDER, project + no)))
            file_name = data['0']['file_name']
            patch_type = data['0']['patch_type']
            # 初始化提示文本，还他妈用example文件，真牛逼
            initial_prompt = INITIAL_APR_TOOL + INTIIAL_APR_EXAMPLE + get_example('Lang_example.txt')
            single_line = False
            # 处理替换类型的补丁
            if patch_type == PATCH_TYPE_REPLACE:
                from_line_no = data['0']['from_line_no']
                to_line_no = data['0']['to_line_no']
                original_buggy_hunk = data['0']['replaced']
                source_file_path = os.path.join(BUGGY_PROJECT_FOLDER, project + no, file_name)
                buggy_function = get_buggy_function(source_file_path, from_line_no, to_line_no, PATCH_TYPE_REPLACE)
                # 构建初始提示
                # 单行补丁
                if from_line_no == to_line_no:
                    single_line = True
                    initial_prompt += INITIAL_Single_line + buggy_function + INITIAL_Single_line_2 + original_buggy_hunk
                # 单块补丁
                else:
                    initial_prompt += INITIAL_Single_hunk + buggy_function + INITIAL_Single_hunk_2 + original_buggy_hunk
            # 处理删除类型的补丁
            if patch_type == PATCH_TYPE_DELETE:
                from_line_no = data['0']['from_line_no']
                to_line_no = data['0']['to_line_no']
                next_line_no = data['0']['next_line_no']
                source_file_path = os.path.join(BUGGY_PROJECT_FOLDER, project + no, file_name)
                buggy_function = get_buggy_function(source_file_path, from_line_no, next_line_no, PATCH_TYPE_DELETE)
                initial_prompt += INITIAL_Single_function + buggy_function
            # 处理插入类型的补丁
            if patch_type == PATCH_TYPE_INSERT:
                next_line_no = data['0']['next_line_no']
                source_file_path = os.path.join(BUGGY_PROJECT_FOLDER, project + no, file_name)
                buggy_function = get_buggy_function(source_file_path, next_line_no, next_line_no, PATCH_TYPE_INSERT)
                initial_prompt += INITIAL_Single_function + buggy_function

            # 添加失败测试信息
            failure_info = prompt_add_failure_test_info(project, json_file)
            if failure_info != '':
                initial_prompt += failure_info
            else:
                return ''
            # 完成初始提示的构建
            if patch_type == PATCH_TYPE_REPLACE or patch_type == PATCH_TYPE_INSERT:
                if single_line:
                    initial_prompt += INITIAL_Single_line_final
                else:
                    initial_prompt += INITIAL_Single_hunk_final
            else:
                initial_prompt += INITIAL_Single_function_final
            return initial_prompt            
        else:
            return ''

# 构建单行补丁的初始提示
def construct_single_function_initial_prompt(project, json_file):
    global previous_failure_test
    # 读取对应的 JSON 文件
    no = json_file.rstrip('.json')
    print("reading json file:",os.path.join(PATCH_JSON_FOLDER, project, json_file))
    with open(os.path.join(PATCH_JSON_FOLDER, project, json_file), 'r', encoding="latin-1") as f:
        data = json.load(f)
        f.close()
    # 如果对应的bug文件夹不存在，运行 defects4j checkout
    if not os.path.exists(os.path.join(BUGGY_PROJECT_FOLDER, project + no)):
        os.system(DEFECTS4J_CHECKOUT % (project, no + 'b', os.path.join(BUGGY_PROJECT_FOLDER, project + no)))
    # 初始化提示文本
    initial_prompt = INITIAL_APR_TOOL + INTIIAL_APR_EXAMPLE + get_example('Lang_single_function_example.txt')
    next_line_no = data['0']['next_line_no']
    file_name = data['0']['file_name']
    # 如果file_name以/开头
    if file_name.startswith('/'):
        base_path = "/ymy/test/patch"
        file_name = os.path.relpath(file_name, base_path)

    source_file_path = os.path.join(BUGGY_PROJECT_FOLDER, project + no, file_name)
    # print("no",no)
    # print("project",project)
    # print("BUGGY_PROJECT_FOLDER",BUGGY_PROJECT_FOLDER)
    # 定义你希望保留的前缀路径
    # base_path = "/ymy/test/patch"
    # # 打印当前工作的目录的路径
    # print("当前工作的目录的路径",os.getcwd())
    # # 使用 relpath 来计算相对路径
    # source_file_path = os.path.relpath(source_file_path, base_path)
    # # 在当前的source_file_path前加上project_name和project_num
    # print("project_name",project_name)
    # print("project_num",project_num)
    # source_file_path = os.path.join(project_name+project_num,source_file_path)
    # source_file_path = os.path.join("bugs",source_file_path)
    # print("source_file_path",source_file_path)

    # 获取有问题的函数
    buggy_function = get_buggy_function(source_file_path, next_line_no, next_line_no, PATCH_TYPE_DELETE)
    # 添加失败测试信息
    failure_info = prompt_add_failure_test_info(project, json_file)
    if failure_info != '':
        initial_prompt += INITIAL_Single_function + buggy_function + failure_info + INITIAL_Single_function_final
        #print("buggy_function",buggy_function)
        #print("failure_info",failure_info)

    else:
        initial_prompt = ''

    return initial_prompt
    

def prompt_add_failure_test_info(project, json_file):
    global previous_failure_test
    # 从 JSON 文件名中去掉 .json 后缀，得到 bug 的编号
    no = json_file.rstrip('.json')
    # 构建失败测试文件的路径
    failure_test_path = os.path.join(BUGGY_PROJECT_FOLDER, project + no, FAILING_TEST_FILE)
    
    # 如果失败测试文件不存在或为空，执行编译测试命令
    if is_file_empty_or_not_exists(failure_test_path):
        os.system('cd ' + os.path.join(BUGGY_PROJECT_FOLDER, project + no) + ' && ' + DEFECTS4J_COMPILE_TEST)
    
    # 获取失败测试的信息，包括测试名称、错误信息、测试文件和行号
    failure_test, test_error, test_file, test_line_no = get_failure_test_info(failure_test_path)
    
    # 如果无法获取测试文件或行号，记录错误日志并返回空字符串
    if test_file == '' or test_line_no == '':
        print("Wrong!!! Unable to handle file:[" + failure_test_path + '] while construct the initial prompt.')
        with open(LOG_FILE, 'a') as file:
            file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + 
                       "\nWrong!!! Unable to handle file [" + failure_test_path + "] while construct the initial prompt.")
            file.close()
            return ''
    
    # 设置全局变量 previous_failure_test 为当前的失败测试
    previous_failure_test = failure_test
    
    # 构建测试文件的完整路径，尝试使用两个不同的前缀
    file = os.path.join(BUGGY_PROJECT_FOLDER, project + no, TEST_FILEPATH_PREFIX[project], test_file)
    if is_file_empty_or_not_exists(file):
        file = os.path.join(BUGGY_PROJECT_FOLDER, project + no, TEST_FILEPATH_PREFIX_1, test_file)
    
    # 根据测试行号，读取测试文件中的相关行
    test_lines = []
    with open(file, mode='r', encoding='latin-1') as test_file:
        lines = test_file.readlines()[test_line_no - 1:]
        for line in lines:
            test_lines.append(line)
            # 当行中包含分号时，停止读取
            if re.sub(r'\".*?\"', '', line).count(';') == 1:
                break
    
    # 返回构建的失败测试信息字符串
    return Failure_Test + failure_test + Failure_Test_line + ''.join(test_lines) + Failure_Test_error + test_error


# Construct the buggy function string with or without the INFILL flag
def get_buggy_function(file_path, from_line_no, to_line_no, patch_type):
    # # 获取方法声明所在的行号
    # start_line_no = get_method_declaration_line_no(file_path, from_line_no)
    # # 获取方法的所有行
    # function_lines = get_method_lines(file_path, start_line_no)
    
    # if patch_type == PATCH_TYPE_REPLACE:
    #     # 删除指定范围内的行（包括起始行，不包括结束行）
    #     del function_lines[from_line_no - start_line_no:to_line_no - start_line_no + 1]
    #     # 在删除的位置插入 INFILL 标记
    #     function_lines.insert(from_line_no - start_line_no, INFILL)
    
    # if patch_type == PATCH_TYPE_INSERT:
    #     # 在指定行插入 INFILL 标记
    #     function_lines.insert(to_line_no - start_line_no, INFILL)
    
    # # 返回拼接后的函数字符串
    # return ''.join(function_lines)
    # 获取方法声明所在的行号
    start_line_no = get_method_declaration_line_no(file_path, from_line_no)
    print("file_path",file_path)
    print("from_line_no",from_line_no)
    print("start_line_no",start_line_no)
    # 获取方法的所有行
    function_lines = get_method_lines(file_path, start_line_no)
    
    if patch_type == PATCH_TYPE_REPLACE:
        # 删除指定范围内的行（包括起始行，不包括结束行）
        del function_lines[from_line_no - start_line_no:to_line_no - start_line_no + 1]
        # 在删除的位置插入 INFILL 标记
        function_lines.insert(from_line_no - start_line_no, INFILL)
    
    if patch_type == PATCH_TYPE_INSERT:
        # 在指定行插入 INFILL 标记
        function_lines.insert(to_line_no - start_line_no, INFILL)
    
    # 返回拼接后的函数字符串
    return ''.join(function_lines)



# Construct information related to failing test based on the implementation of chat repair (only considers one failing test)
def get_failure_test_info(test_file_path):
    with open(test_file_path, 'r', encoding='latin-1') as file:
        lines = file.readlines()
        failing_test = lines[0].strip('--- ').rstrip()
        test_error = lines[1].rstrip()
        test_function = failing_test.split("::")[1].rstrip()
        # test_file = failing_test.split("::")[0].replace('.', '/') + '.java'
        for i in range(2, len(lines)):
            if test_function in lines[i]:
                try:
                    test_line_no = int(re.search(r'(\d+)\)', lines[i]).group(1))
                    test_file = delete_substring_to_end(lines[i],'.'+test_function).split('at ')[1].replace('.', '/') + '.java'
                    return failing_test, test_error, test_file, test_line_no
                except AttributeError as e:
                    print("Warning!!! Unable to handle file [" + test_file_path + "]while get the the test info:",e)
                    with open(LOG_FILE, 'a') as file:
                        file.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"\nWarning!!! Unable to handle file [" + test_file_path + "] while get the the test info.")
                        file.close()
                    return failing_test, test_error, '', ''
        # Non-compliant failing_test file
        return failing_test, test_error, '', ''

# Find the line number of the method declaration in the source code file
def get_method_declaration_line_no(source_file_path, line_no):
    with open(source_file_path, "r",encoding="latin-1") as file:
        source_code = file.read()
        file.close()
    tree = parse.parse(source_code)
    line_nos = []
    start_line_no = 0
    for path, node in tree.filter(MethodDeclaration):
        line_nos.append(node.position.line)
    for i in range(0, len(line_nos) - 1):
        if line_nos[i] <= line_no <= line_nos[i + 1]:
            start_line_no = line_nos[i]
    if start_line_no == 0:
        start_line_no = line_nos[len(line_nos) - 1]
    return start_line_no


# Get the lines of the corresponding function in the source code file
def get_method_lines(source_file_path, start_line_no):
    # with open(source_file_path, "r", encoding='latin-1') as file:
    #     lines = file.readlines()[start_line_no - 1:]
    #     if start_line_no == 788:
    #         print("lines",lines)
    #     file.close()
    # left_open_brackets = 0
    # right_open_brackets = 0
    # function_lines = []
    # for line in lines:
    #     function_lines.append(line)
    #     left_open_brackets += line.count('{')
    #     right_open_brackets += line.count('}')
    #     if left_open_brackets == right_open_brackets and not left_open_brackets == 0:
    #         break
    # return function_lines
    with open(source_file_path, "r", encoding='latin-1') as file:
        all_lines = file.readlines()
    
    # 获取函数部分（保持原有逻辑）
    function_lines = []
    lines = all_lines[start_line_no - 1:]
    left_open_brackets = 0
    right_open_brackets = 0
    
    for line in lines:
        function_lines.append(line)
        left_open_brackets += line.count('{')
        right_open_brackets += line.count('}')
        if left_open_brackets == right_open_brackets and not left_open_brackets == 0:
            break
    
    # 向上找注释部分
    comment_lines = []
    current_line = start_line_no - 2  # 从函数定义的上一行开始向上查找
    
    # 先跳过空行
    while current_line >= 0 and all_lines[current_line].strip() == '':
        current_line -= 1
    
    # 收集注释行
    comment_found = False
    while current_line >= 0:
        line = all_lines[current_line]
        
        # 如果是注释行，添加到注释列表
        if line.strip().startswith('/*') or line.strip().startswith('*') or line.strip().startswith('*/'):
            comment_lines.insert(0, line)  # 插入到列表前面，保持顺序
            comment_found = True
        # 如果找到了注释开始后又遇到非注释行，说明注释已经结束
        elif comment_found:
            break
        # 如果还没找到注释，但遇到了非注释行，继续向上查找
        else:
            # 如果是双斜杠注释（如 // Equals），也收集
            if line.strip().startswith('//'):
                comment_lines.insert(0, line)
            else:
                # 遇到非注释行且还没找到注释的开始，则停止
                if not comment_found:
                    break
        
        current_line -= 1
    
    # 合并注释和函数
    return comment_lines + function_lines
    

def get_example(example_file):
    with open(example_file, 'r') as f:
        example = f.read()
        f.close()
        return example

if __name__ == '__main__':
    ins, p, all = sys.argv[1:4]
    project_name = p
    if ins not in ["chatrepair", "initial-save", "initial-chat"]:
        print("Instruction only support \"chatrepair\"and\"initial-save\" and \"initial-chat\"")
    else:
        if p not in PROJECTS:
            print("Project only support these:\n")
            print(PROJECTS)
        else:
            if ins == "initial-save" and all == 'y':
                save_initial(p,True)
            elif ins == "initial-save" and all == 'n':
                save_initial(p,False)
            elif ins == "initial-chat" and all == 'y':
                chat_initial(p, True)
            elif ins == "initial-chat" and all == 'n':
                chat_initial(p, False)
            elif ins == "chatrepair" and all == 'y':
                go_chat_repair(p,True)
            elif ins == "chatrepair" and all == 'n':
                go_chat_repair(p, False)


def get_method_bounds(source_file_path, start_line_no):
    """
    返回源文件中指定方法的起始行号和结束行号（不包含注释）。

    Args:
        source_file_path (str): 源代码文件路径
        start_line_no (int): 方法声明所在的起始行号（1-indexed）

    Returns:
        tuple: (start_line_no, end_line_no)
    """
    # 读取整个文件内容
    with open(source_file_path, 'r', encoding='latin-1') as f:
        all_lines = f.readlines()

    # 获取方法及其注释的所有行
    method_lines = get_method_lines(source_file_path, start_line_no)
    #print("method_lines",method_lines)
    m_len = len(method_lines)
    # 在文件中寻找 method_lines 匹配的位置
    for idx in range(len(all_lines) - m_len + 1):
        if all_lines[idx: idx + m_len] == method_lines:
            start_no = idx + 1            # 转为 1-based 行号
            end_no = idx + m_len          # 转为 1-based 行号
            return start_no, end_no

    # 若未找到，则抛出异常
    raise ValueError(f"Method lines not found in {source_file_path}")

