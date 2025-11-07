def mostFreqChar(s):
    dict = {}
    count = 0
    most_frq=None
    for char in s:
        if char not in dict:
            dict[char] = 0
        dict[char]+=1
    print(count)
    
    for char in s:
        if dict[char]>count:
            most_frq = char
            count = dict[char]
    return most_frq

s = 'potato'
print(mostFreqChar(s))

