def largestRange(array):
    # Write your code here.
    array.sort()
    ref=array[0]
    rangeList=[]
    maxRange=0
    ini=ref
    ending=array[0]
    
    if len(array)>1:
        for i in range(1,len(array)):
            if array[i]<=ref+1:
                ending=array[i]
                ref=array[i]
            else:
                rangeList.append([ini,ending])

                ini=array[i]
                ref=array[i]
                
        
        rangeList.append([ini,ending])
        for j in range(0,len(rangeList)):
            if maxRange<(rangeList[j][1]-rangeList[j][0]):
                ini=rangeList[j][0]
                ending=rangeList[j][1]
                maxRange=rangeList[j][1]-rangeList[j][0]
        
    else:
        ini=array[0]
        ending=ini
    
    ans=[ini,ending]
    return ans

array=[0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2]
print(largestRange(array))