"""Problem: Two Sum 
Given nums = [2, 7, 11, 15] and target = 9"""
#using brute force method with O(n^2)
#a nested loop to check pairs
for i in range(len(nums)):  
    for j in range(i + 1, len(nums)):  
        if nums[i] + nums[j] == target:  
            return [i, j]  
          
#using optimal method O(n)
#a dictionary to keep track of the seen numbers
seen = {}  
for i, num in enumerate(nums):  
    complement = target - num  
    if complement in seen:  
        return [seen[complement], i]  
    seen[num] = i  
