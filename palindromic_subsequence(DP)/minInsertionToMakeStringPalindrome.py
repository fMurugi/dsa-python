"""
The approach here is that len(s) -lps
"""
# ===================
# Use of tabulation
# ===================


def minInsertions( s: str) -> int:
    n=len(s)
    dp =[[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] =1
    print(dp)
    for j in range(1,n): #j is end
        for i in range(j-1,-1,-1): #i is end

            if s[i] == s[j]:
                dp[i][j] =2+(dp[i+1][j-1])
            else:
                dp[i][j]= max(dp[i+1][j],dp[i][j-1])
    print(dp)
    lps = dp[0][n-1]
    print(lps)

    return len(s)-lps
minInsertions("adbbca")

# ===================
# cleaner tabulation from the right-bottom conner
# ===================
def minInsertions2( s: str) -> int:
    n=len(s)
    dp =[[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] =1
    print(dp)
    for i in range(n-2,-1,-1): #j is end
        for j in range(i+1,n): #i is end

            if s[i] == s[j]:
                dp[i][j] =2+(dp[i+1][j-1])
            else:
                dp[i][j]= max(dp[i+1][j],dp[i][j-1])
    print(dp)
    lps = dp[0][n-1]
    print(lps)

    return len(s)-lps
print(minInsertions2("adbbca"))


"""
Another intuiton
base cases:
if i>=j: return O this means we have i and j point to one char or we have an empty substring
if we get s[i]==s[j]: move both pointers
if s[i]!=s[j]: 
    we add the char at s[i] after j and then move i to s[i+1] and remain s[j]
    OR
    we add the char at j before i then move j and dont move i s[i] and s[j-1]

    we take minimum of the two above scenarios

"""
s ="adbbca"
from functools import cache
@cache
def minInsertion3(s):
    n=len(s)
    def dfs(i,j):
        if i>=j:
            return 0
        if s[i] == s[j]:
            return dfs(i+1,j-1)
        else:
            return 1+min(dfs(i+1,j),dfs(i,j-1))
    return dfs(0,n-1)
ans = minInsertion3(s)
print(ans)
"""
Time complexity:
Note: without @cache for memoization this is pure recursion and has time complexity of exponential(2^n)
i can go from 0 to n-1, and j can go from 0 to n-1.
So the total number of possible subproblems is roughly O(n^2) (all pairs (i,j) with i ≤ j).

Space compleixty
Memoization cache: The @cache decorator stores up to O(n^2) unique states, each taking O(1) space to store the result.
Recursion stack: In the worst case, the recursion depth can be O(n) when we continuously move either i forward or j backward without finding matching characters.
"""