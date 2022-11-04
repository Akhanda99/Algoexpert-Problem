def firstDuplicateValue(array):
    # Write your code here.
    minindex=9999
    for i in range(0,len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]==array[j] and j<minindex:
                minindex=j
            else:
                continue

    try:
        ans=array[minindex]
    except:
        ans=-1
        
    return ans

array=[2, 1, 5, 2, 3, 3, 4]
print(firstDuplicateValue(array))

array=[2]
print(firstDuplicateValue(array))