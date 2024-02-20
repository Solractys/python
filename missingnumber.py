nums = [9,6,4,2,3,5,7,0,1]

def missingNumber(nums: list):
    sorted(nums)
    n = len(nums) - 1
    for i in range(n):
        future = i
        if nums[i] != future:
            return future
    return n
            
    
print(missingNumber(nums))