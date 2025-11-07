def pairProd(nums,targetProd):
    seen ={}
    for index,num in enumerate(nums):
        complement = targetProd/num
        if complement in seen:
            return (seen[complement],index)
        seen[num] = index

print(pairProd([3,2,5,4,1],8))

# linear time and space complexity
