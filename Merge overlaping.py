def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort()
    a=intervals[0][0]
    b=intervals[0][1]
    ans=[]
    for i in range(0,len(intervals)):
        if intervals[i][0]>b:
            ans.append([a,b])
            a=intervals[i][0]
            b=intervals[i][1]
        else:
            if b>intervals[i][1]:
                continue
            else:
                b=intervals[i][1]
    ans.append([a,b])
    return ans

#Test Case
array=[
    [2, 3],
    [4, 5],
    [6, 7],
    [8, 9],
    [1, 10]
  ]

print(mergeOverlappingIntervals(array))
