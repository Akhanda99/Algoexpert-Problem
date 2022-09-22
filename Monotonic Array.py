def isMonotonic(array):
    # Write your code here.
    ans=True
    inc=0
    dec=0
    eq=0
    if len(array)>0:
        for i in range(0,len(array)-1):
            if array[i+1]==array[i]:
                eq+=1
            elif array[i+1]>array[i]:
                inc+=1
            else:
                dec+=1
        if inc==len(array)-eq-1 or dec==len(array)-eq-1 or eq==len(array)-1:
            ans=True
        else:
            ans=False
    return ans
            

#Test Case 01
array= [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print(isMonotonic(array))