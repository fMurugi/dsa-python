# return true if two strings are anagrams
from collections import Counter
def is_anagram(s,t):
    return sorted(s) == sorted(t) # O(nlogn) to sort the strings

print(is_anagram("tea","eat"))


def is_anagram1(s,t):
    return Counter(s) == Counter(t) #time -> O(N) to create the dict
#Space complexity: O(1) (since there are at most 26 lowercase letters if the input is limited to English).

print(is_anagram1("tea","eat"))

#counting

def is_anagram3(s,t):
    count1 = [0]*26
    
    for c in s:
        count1[ord(c)-ord('a')] +=1
    for c in t:
        count1[ord(c)-ord('a')]-=1
    return all(c ==0 for c in count1)

print(is_anagram3('tea','eat'))


