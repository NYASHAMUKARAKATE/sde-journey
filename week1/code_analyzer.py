"""
A friendly Python script that analyzes your code files.
It counts how many files you have and how many lines of actual code you've written,
ignoring empty lines and comments.
"""

import os
from collections import defaultdict



def analyze_code(folder_path):
    """
    Analyzes all Python files in a directory and its subdirectories.
    Returns dictionary with these keys:
    - files: Total Python files found
    - lines: All lines (including comments/empty)
    - code: Only lines with actual code
    - functions: Number of function definitions
    - classes: Number of class definitions
    """
    stats = {
        'files': 0,
        'lines': 0,
        'code': 0,
        'functions': 0,
        'classes': 0
    }
    
    for item in os.listdir(folder_path):
        path = os.path.join(folder_path, item)
        
        if os.path.isdir(path):
            sub_stats = analyze_code(path)
            for k in stats:
                stats[k] += sub_stats[k]
                
        elif item.endswith('.py'):
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line: continue
                    
                    stats['lines'] += 1
                    if not line.startswith('#'):
                        stats['code'] += 1
                        if 'def ' in line: stats['functions'] += 1
                        if 'class ' in line: stats['classes'] += 1
            stats['files'] += 1
            
    return stats

# Print results using the CORRECT keys
stats = analyze_code('.')
print("\n📊 Final Results:")
print(f"- Total Python files: {stats['files']}")
print(f"- Total lines: {stats['lines']}")
print(f"- Actual code lines: {stats['code']}")
print(f"- Functions: {stats['functions']}")
print(f"- Classes: {stats['classes']}")