import os  

def count_py_files(path):  
    total = 0  
    for entry in os.listdir(path):  
        full_path = os.path.join(path, entry)  
        if os.path.isdir(full_path):  
            total += count_py_files(full_path)  # Recursion!  
        elif entry.endswith(".py"):  
            total += 1  
    return total  

print(count_py_files(sde-journey))
