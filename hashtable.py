
# def single_number(nums):
#     xor_result = 0
#     for num in nums:
#          xor_result ^= num
#     print(xor_result)

# nums = [1, 1 , 2, 3, 3, 4, 4]

# single_number(nums)

def findTheDifference(s: str, t: str) -> str:
        if len(s) == None:
            return t
        xor_result = 0
        for c in s + t:
            xor_result ^= ord(c)
        result = chr(xor_result)
        print (result)

s = "a"
t = "aa"

findTheDifference(s, t)