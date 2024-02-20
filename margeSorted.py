nums1 = [-1,0,0,3,3,3,0,0,0]
nums2 = [1, 2, 2]
m = 6
n = 3
def merge(nums1: list[int], nums2: list[int], m: int, n: int):
    i, j = m - 1, n - 1
    k = len(nums1) - 1
    while j >= 0 and i >= 0:
        if nums2[j] >= nums1[i]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
        k -= 1
    nums1[:j + 1] = nums2[:j + 1] 
    
    print(nums1)
    
merge(nums1, nums2, m, n)