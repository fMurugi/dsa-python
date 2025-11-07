
intervals =[ [5,7],[1,3], [8,12]]
output =[]
intervals.sort(key=lambda x:x[0])
def insert_interval(interval):
    #skip and add to output all intervals that come before this interval
    i=0
    n= len(intervals)
    while i<n and interval[0] > intervals[i][1]: # while i <n and interval[i] ends before interval[i] start
        output.append(intervals[i])
        i+=1
    
    # merge all intervals that overlap with interval
    while i<n and intervals[i][0] <= interval[1]:
        interval[0] = min(interval[0],intervals[i][0])
        interval[1]  = max(interval[1],intervals[i][1])
        i+=1
    output.append(interval)

    # add all the remaining intervals to the output
    while i<n:
        output.append(intervals[i])
        i+=1


    return output

ans = insert_interval([4,10])
print(ans)