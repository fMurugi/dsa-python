# elements that occur in two arrays
# [3,2,5,6], [2,1,4,6] -> [2,6]

# first soln: if for every element in array a we search it in array b, then:
# time complexity = O(n*m) since the arrays do not have the same length
# space complexity = o(min(n,m)) the spaces to store the common elements will be atmost  equal to the smallest array

def intersection(nums1,nums2):
    common_nums =[]
    nums1_set = set(nums1) #O(n)  #space O(n)
    for num in nums2:#o(m)
        if num in nums1_set: # conatnt time look up in sets
            if num not in common_nums: # to deal with duplicates
                common_nums.append(num) #space -> O(min(m,n))
    return common_nums

print(intersection([4,2,1,6],[3,6,9,2,10]))
print(intersection([1,2,3],[2,2,2,3]))

#using sets the time complexity is O(n+m)



def intersection2(nums1,nums2):
    set1 = set(nums1) 
    set2 = set(nums2)
    return set1.intersection(set2)

print(intersection2([4,2,1,6],[3,6,9,2,10]))
print(intersection2([1,2,3],[2,2,2,3]))

def intersection3(nums1,nums2):
    nums1_set = set(nums1) #O(n)  #space O(n)
    # return [ele for ele in nums2 if ele in nums1_set]
    return list(set(num for num in nums2 if num in nums1_set)) #deal with duplicates
print(intersection3([4,2,1,6],[3,6,9,2,10]))
print(intersection3([1,2,3],[2,2,2,3]))

"""No, space is O(n + k), not O(min(n, m))
Where k ≤ min(n, m) is the size of the intersection.
Space Breakdown:

nums1_set = set(nums1) → O(n) space
common_nums list → O(k) space, where k ≤ min(n, m)

Total = O(n + k) = O(n + min(n, m))"""
