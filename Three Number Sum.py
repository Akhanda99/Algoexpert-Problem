def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    result=[]
    for i in range(0,len(array)-2):
        main=array[i]
        need=targetSum-array[i]
        array.remove(main)
        for j in range(i+1,len(array)):
            sub_res=[]
            num1=array[j]
            num2=need-array[j]
            array.remove(num1)
            if num2 in array:
                sub_res.append(main)
                sub_res.append(num1)
                sub_res.append(num2)
                sub_res.sort()
                if sub_res in result:
                    pass
                else:
                    result.append(sub_res)
            array.append(num1)
            array.sort()
        array.append(main)
        array.sort()
    result.sort()
    return result
    
#Test Case
array=[12,3,1,2,-6,5,-8,6]
targetSum=0
result=threeNumberSum(array,targetSum)
print(result)