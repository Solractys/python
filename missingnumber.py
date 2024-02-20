nums = [3, 0, 1]

def missingNumber(nums: list):
    nums.sort()
    n = len(nums)
    for i in range(n):
        future = i
        if nums[i] != future:
            return future
    return n
            
    
print(missingNumber(nums))