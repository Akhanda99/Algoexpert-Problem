def subarraySort(array):
    # Write your code here.
    upp=0
    low=0
    count=0
    ans=[]
    max=-9999
    maxIndex=0
    for i in range(0,len(array)):
        current=array[i]
        if current>=array[maxIndex]:
            max=current
            maxIndex=i
        
        else:
            count+=1
            
            if count>1:
                upp=i
            else:
                upp=i
                low=maxIndex
            for j in range(0,low):
                    if array[upp]>=array[j]:
                        continue
                    else:
                        low=j
                        break
        

    if count>0:
        ans=[low,upp]
    else:
        ans=[-1,-1]
    return ans



array=[1, 2]
print(subarraySort(array))

array=[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(subarraySort(array))