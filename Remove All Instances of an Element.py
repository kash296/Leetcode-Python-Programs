def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return(len(nums),nums)

num = [3,2,3,4,3,3,3,3,6,2,3,3,7]
v = 3
print(removeElement(num,v))