def sortedSquaredArray(array):
    # Write your code here.
    ansarray=[]
    for i in range(0,len(array)):
        value=array[i]**2
        ansarray.append(value)
    return sorted(ansarray)

#test case 01
array= [1, 2, 3, 5, 6, 8, 9]
print(sortedSquaredArray(array))

#test case 02
array1=[-2, 1]
print(sortedSquaredArray(array1))