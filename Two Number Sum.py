def twoNumberSum(array, targetSum):
    # Write your code here.
    ans=[]
    for i in range(0,len(array)):
        a=array[i]
        b=targetSum-array[i]
        array.remove(a)
        if b in array:                    
            ans.append(a)
            ans.append(b)
            ans.sort()
            break
        else:
            array.insert(i,a)
    return ans

#Test 1
array= [4, 6, 1, -3]
targetSum= 3
print(twoNumberSum(array, targetSum))
