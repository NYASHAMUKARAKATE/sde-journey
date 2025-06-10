import os  

def count_py_files(path):  
    total = 0  
    for entry in os.listdir(path):  
        full_path = os.path.join(path, entry)  
        if os.path.isdir(full_path):  
            total += count_py_files(full_path)  
        elif entry.endswith(".py"):  
            print(f"Found Python file: {full_path}")
            total += 1  
    return total  

print(f"Total .py files: {count_py_files('.')}")  