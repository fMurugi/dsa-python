def twoSum(nums,targetSum):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j] == targetSum:
                return (i,j)


print(twoSum([3,3],6))


def twoSumOptimal(nums,targetSum):
    seen ={}
    for index,num in enumerate(nums): #(index, num) index then item Not the other way
        complement = targetSum - num
        if complement in seen:
            return (seen[complement],index)

        seen[num]=index #store the num as key and index as value not complement as key

print(twoSumOptimal([2,7,11,15],9))
