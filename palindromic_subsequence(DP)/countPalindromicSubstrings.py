"""
Given a string, find the total number of palindromic substrings in it. Please note we need to find the total number of substrings and not subsequences.

Example 1:

Input: "abdbca"
Output: 7
Explanation: Here are the palindromic substrings, "a", "b", "d", "b", "c", "a", "bdb".

Example 2:
Input: = "pqr"
Output: 3
Explanation: Here are the palindromic substrings,"p", "q", "r".

"""

def countPalindromicSub(s):
    n = len(s)
    def checkIfpalindrome(i,j):
        temp_count =0 # remmembert to declare this
        while ((i>=0 and j<n) and s[i]==s[j] ):
            temp_count+=1
            i-=1
            j+=1
        return temp_count  #remember to return this
    
    count = 0
    for i in range(n):
        count+=checkIfpalindrome(i,i)
        count+=checkIfpalindrome(i,i+1)
    return count
print(countPalindromicSub("abdbca"))
print(countPalindromicSub("cddpd"))
print(countPalindromicSub("pqr"))


