# list -> ["eat", "tea", "tan", "ate", "nat", "bat"]
from collections import defaultdict
def group_anagrams(anagrams):
    groups = defaultdict(list)

    for s in anagrams: #O(n)
        groups["".join(sorted(s))].append(s) #O(klogk)
    return list(groups.values())
#time complexity is O(N*klogk)
# Space complexity is O(Nk) because we store all N strings and also store the sorted version of each string as a key, each of size k.

"""NOTES
strings do not have a method sort(), so not s.sort() strings are immutable and cannot be sorted in place
"""

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))



# with counting
def group_anagrams2(anagrams):
    groups = defaultdict(list) #o(n)
    for s in anagrams: #O(n)
        count = [0] *26 #constant
        for c in s:#o(k)
            count[ord('a')-ord(c)] +=1
        key = tuple(count)
        groups[key].append(s)
    return list(groups.values())
print(group_anagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))

#time complexity is O(n*k)