"""
given a string "abc" return the length of the longest palindromic subsequence
"""

#brute force
"""
Generate all the subsequnces using recusrion 
Check each subsequence to see if it is a palindrome
Maintain a var max_len and return this eventually

This is a bruteforce method and will use time compleixty: O(2^n)
and space O(2^n *n) to store all the subsequnces which asre 2^n and each subsequqnce may take atmost O(n)
Plus the recursion stack will be O(n) which is the height if the tree
""" 

def lps_brute(s):
    subsequnces =[]
    temp=[]
    def generate_subsequences(i,s):
        
        if i ==len(s):
            subsequnces.append("".join(temp.copy()))
            return
        
        temp.append(s[i])
        generate_subsequences(i+1,s)
        temp.pop()
        generate_subsequences(i+1,s)
    generate_subsequences(0,s)

    max_len =0
    print(subsequnces)

    for sub in subsequnces:
        if sub == sub[::-1]:
            max_len = max(max_len,len(sub))
    return max_len

print(lps_brute("abca"))


#=======================================================================
# recursion
#=======================================================================

"""
just like LCS
"""


def lps(s):
    n = len(s)
    def solve(i,j):
        if i>j:
            return 0
        if i == j:
            return 1
        if s[i]==s[j]:
            return 2+solve(i+1,j-1)
        else:
            return max(solve(i+1,j),solve(i,j-1))
    return solve(0,n-1)
print(lps("abbca"))
print(lps("abca"))
print(lps("bbbab"))


#=======================================================================
# memoization
#=======================================================================

print("=======MEMOIZATION========")
def lpsmemo(s):
    n = len(s)
    dp = [[-1]*n for _ in range(n)]
    def solve(i,j):
        if i>j:
            return 0
        if i == j:
            return 1
        if dp[i][j]!=-1:
            return dp[i][j]
        if s[i]==s[j]:
            dp[i][j] =2+solve(i+1,j-1)
        else:
            dp[i][j] = max(solve(i+1,j),solve(i,j-1))
        return dp[i][j]
    return solve(0,n-1)
print(lpsmemo("abbca"))
print(lpsmemo("abca"))
print(lpsmemo("bbbab")) 



#=======================================================================
# Tabulation
#=======================================================================














#=======================================================================
# USE LCS code
#=======================================================================

