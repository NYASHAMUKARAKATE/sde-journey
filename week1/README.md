# Day 2: Recursion & Memoization  
### 🎯 Key Learnings  
- Memoization reduced Fibonacci time from O(2ⁿ) to O(n)  
- Benchmark Results 
  | Approach   | Time (n=35)   
  ----------------------------------- 
  Naive         1.45 sec     
  Memoized      ~0.000001 sec (0.0s)   

### 📝 Code Highlights  
```python  
# Manual memoization  
memo = {}  
def fib_memo(n):  
    if n in memo:  
        return memo[n]  # Cache found 
    if n <= 1:  
        return n  
    memo[n] = fib_memo(n-1) + fib_memo(n-2)  # Store result  
    return memo[n]  