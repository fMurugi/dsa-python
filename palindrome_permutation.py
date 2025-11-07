
# checking if a string permutation/ rearrangement of a character string  can form palindrome 
# https://algo.monster/liteproblems/266
# learnt:  characters of a string that can form a palindrome should have atmost one character that has a frequency of odd, the rest msut be even
# and using & 1 with the frequency you get 0 or 1 , if a number is odd the signed bit is 1 sor 1& 1 becomes 1 
# because odd numbers have their least significant bit set to 1

from typing import Counter

def palindrome(s):
    freq = Counter(s)

    total = sum(v&1 for k,v in freq.items())
    print(total)
    if total<2:
        return True
    return False

ans = palindrome("aba")
print(ans)