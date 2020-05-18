def twoSum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i

num = [2,7,11,15]
tar = 18
print(twoSum(num,tar))