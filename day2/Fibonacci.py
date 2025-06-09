#Recursion and memoisation 
"""Optimizing the  Fibonacci
naive recursive fib(n) (O(2ⁿ)).
Implementing memoization manually (using a dictionary).
comparing the execution times for n = 35."""

import time  

# Naive recursive  
def fib(n):  
    if n <= 1:  
        return n  
    return fib(n - 1) + fib(n - 2)  

# Manual memoization  
memo = {}  
def fib_memo(n):  
    if n in memo:  
        return memo[n]  
    if n <= 1:  
        return n  
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)  
    return memo[n]  

# Benchmark  
start = time.time()  
print(fib(35))  
print("Naive time:", time.time() - start)  

start = time.time()  
print(fib_memo(35))  
print("Memo time:", time.time() - start)  

