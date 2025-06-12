import os

ignore_dirs = {".git", "__pycache__"}

def count_py_files(path):
    total = 0
    for entry in os.listdir(path):
        if entry in ignore_dirs:
            continue
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            total += count_py_files(full_path)
        elif entry.lower().endswith(".py"):
            try:
                with open(full_path, "r", encoding="utf-8") as f:  # Force UTF-8
                    lines = len(f.readlines())
                print(f"Found: {full_path} ({lines} lines)")
                total += 1
            except UnicodeDecodeError:
                print(f"Skipped: {full_path} (invalid encoding)")
    return total

print(f"\nTotal .py files: {count_py_files('.')}")