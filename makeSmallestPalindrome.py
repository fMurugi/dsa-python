def makeSmallestPalindrome(s: str) -> str:
    n = len(s)
    list_s= list(s)
    i = 0
    j = n-1
    while i<j:
        if list_s[i]!=list_s[j]:
            list_s[i] = min(list_s[i],list_s[j])
            list_s[j] =  min(list_s[i],list_s[j])
        i+=1
        j-=1
    return list_s

ans = makeSmallestPalindrome("abcd")
print("".join(ans))
