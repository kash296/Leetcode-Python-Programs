def merge(nums1, m, nums2, n):
    print(nums1[:m])
    nums1[m:] = nums2[:n]
    nums1.sort()
    #return(nums1)

num1=[1,2,3,0,0,0]
num2=[2,5,6]
m=3
n=3

print(merge(num1,m,num2,n))
