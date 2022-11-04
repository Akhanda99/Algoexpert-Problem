def firstDuplicateValue(array):
    # Write your code here.
    dList=[]
    ans=-1
    for i in range(0,len(array)):
        if array.count(array[i])>0:
            if len(dList)==0:
                dList.append(array[i])
            else:
                if array[i] in dList:
                    ans=array[i]
                    break
                else:
                    dList.append(array[i])
    
    return ans

array=[2, 1, 5, 2, 3, 3, 4]
print(firstDuplicateValue(array))

array=[2]
print(firstDuplicateValue(array))