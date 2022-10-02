def longestPeak(array):
    # Write your code here.
    highestlength=0
    
    high=0
    low=0
    highestlengthList=[]
    sortedArray=sorted(array)
    if sortedArray==array:
        highestlength=0
    else:
        for i in range(0,len(array)-1):
            if array[i+1]-array[i]!=0:
                if array[i+1]-array[i]<0:
                    if high>0:
                        low+=1
                    else:
                        pass
                elif array[i+1]-array[i]>0:
                    if high>0 and low>0:
                        length=high+low
                        highestlengthList.append(length)
                        high=low=0
                        high+=1
                    else:
                        high+=1
            elif array[i+1]-array[i]==0:
                if high>0 and low>0:
                    length=high+low
                    highestlengthList.append(length)
                high=0
                low=0
    if high>0 and low>0:
        length=low+high
        highestlengthList.append(length)
    if len(highestlengthList)!=0:    
        highestlength=max(highestlengthList)+1
    
    return highestlength



# array=[1, 2, 3, 4, 5, 1]
array=[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
longestPeak=longestPeak(array)
print(longestPeak)