
import subprocess
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_bug_ids(project):
    try:
        result = subprocess.run(
            ['defects4j', 'bids', '-p', project],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        bug_ids = list(map(int, result.stdout.strip().split()))
        return sorted(bug_ids)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to get bug IDs for project {project}:\n{e.stderr}")
        return []

def run_test_patch(n, project):
    try:
        print(f"🚀 Running test_patch.py for {project} bug {n}")
        subprocess.run(['python3', 'test_patch.py', str(n), project], check=True)
        print(f"✅ Finished bug {n}")
    except subprocess.CalledProcessError:
        print(f"⚠️ test_patch.py failed for {project} bug {n} (continuing...)")

def main():
    parser = argparse.ArgumentParser(description="Batch test LLM patches for a project")
    parser.add_argument("project", help="Project name, e.g., Lang")
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers (default: 4)")
    args = parser.parse_args()

    project = args.project
    workers = args.workers

    bug_ids = get_bug_ids(project)
    if not bug_ids:
        print("❌ No bug IDs found.")
        return

    print(f"🔍 Found {len(bug_ids)} bugs for project {project}. Starting parallel patch testing...")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(run_test_patch, n, project) for n in bug_ids]
        for future in as_completed(futures):
            pass  # Already logged

if __name__ == "__main__":
    main()
