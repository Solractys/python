def permute(nums): 
    inp = []
    k = len(nums)
    def backtrack(start, arr):
        if len(arr)==k:                
            inp.append(arr.copy())
        for i in range(0,len(nums)):
            if nums[i] not in arr:
                arr.append(nums[i])
                backtrack(i+1, arr)
                arr.pop()
    backtrack(0, [])
    return inp