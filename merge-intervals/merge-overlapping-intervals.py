# intervals = [[1,4],[2,5],[7,9]]

# intervals =[[1,5],[2,3],[4,6]]  # everything overlaps

intervals = [[1, 2], [3, 4], [5, 6]]


#ensure they are sorted base on start time such that
# a[start] <= b[start]

# if b[start] <= a[end]
#adjust the end since you are sorting by start and now a[start] is always less than or equal to b[start] just adjust the end only and take a[start]

# else if no overlap just add the interval to the merged intervals/result





def merge_overlapping_intervals(interval):
    result =[]
    interval.sort(key=lambda x:x[0])
    start,end = interval[0]
    for i in range(1, len(interval)):
        cur_start,cur_end = interval[i]
        if cur_start<=end:
            end = max(end,cur_end)
        else:
            # no overlap only add here if there is no overlap
            result.append([start,end])
            start = cur_start
            end = cur_end
    result.append([start,end])
    return result
ans = merge_overlapping_intervals(intervals)
print(ans)



