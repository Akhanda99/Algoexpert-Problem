def arrayOfProducts(array):
    # Write your code here.
    ans=[]
    for i in range(0,len(array)):
        num=array[i]
        array.remove(num)
        mul=1
        for j in range(0,len(array)):
            mul=mul*array[j]
        ans.append(mul)
        array.insert(i,num)
    return ans
            
            

        
array=[5, 1, 4, 2]
ans=arrayOfProducts(array)
print(ans)