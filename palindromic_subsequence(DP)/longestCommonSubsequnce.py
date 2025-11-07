def lcs(text1,text2):
    n = len(text1)
    m = len(text2)

    def solve(i,j):
        if i==n or j ==m:
            return 0
        if text1[i] == text2[j]:
            return 1+solve(i+1,j+1)
        return max(solve(i+1,j),solve(i,j+1))
    
    return solve(0,0)
    
print(lcs("abcde","ace"))
#time complexity -> O(z^(m+n))
#space complexity -> o(m+n) 
        
#memoization
def lcs_memo(text1,text2):
    n = len(text1)
    m = len(text2)
    cache ={} 

    def solve(i,j):
        if i==n or j ==m:
            return 0
        if text1[i] == text2[j]:
            result = 1+solve(i+1,j+1)
        else: #note if you dont put else here this next line is execute even though the chars above are equal
            result = max(solve(i+1,j),solve(i,j+1))

        cache[(i,j)] = result
        return result
    
    return solve(0,0)
    
print(lcs_memo("abcde","ace"))
#time complexity -> O(m*n)
#space complexity -> O(m*n)+o(m+n)
"""
whhy memo uses O(m*n)
text1 = "abc"  (m = 3)
text2 = "ac"   (n = 2)

The memo stores results for UNIQUE (i, j) pairs:
- i can be: 0, 1, 2, 3  (4 values: from 0 to m)
- j can be: 0, 1, 2     (3 values: from 0 to n)

Total possible unique states = 4 × 3 = 12 = (m+1) × (n+1) ≈ O(m×n)
"""

#bottum up
def lcs_dp(text1,text2):
    n = len(text1)
    m = len(text2)

    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1+  dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[n][m]
    
print(lcs_dp("abcde","ace"))

#time complexity(m*n)
#space O(m*n)->dp array

#-----------------------------------   
#space optimized bottumupdp
def lcs_dpOptimized(text1,text2):
    n = len(text1)
    m = len(text2)
    curr = [0] *(m+1)
    prev = [0] *(m+1)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if text1[i-1] == text2[j-1]:
                curr[j] = 1+  prev[j-1] #uses prev diagonal
            else:
                curr[j] = max(prev[j],curr[j-1]) 
        prev,curr = curr,prev
        """
         always remember to put brakcets here to avoid this
         curr = [0] *(m+1)
    prev = [0] *(m+1)
          curr = [0] *m+1
TypeError: can only concatenate list (not "int") to list
"""
            
    return prev[m]
    
print(lcs_dpOptimized("abcde","ace"))