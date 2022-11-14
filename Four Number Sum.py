def fourNumberSum(array, targetSum):
    # Write your code here.
    numberList=[]
    sumPair={}
    for i in range(0,len(array)-1):
        for j in range(i+1,len(array)):
            currentSum=array[i]+array[j]
            diff=targetSum-currentSum
            
            if diff in sumPair:
                for pair in sumPair[diff]:
                    numberList.append(pair+[array[i],array[j]])
        
        for k in range(0,i):
            backSum=array[i]
            backSum+=array[k]
            if backSum in sumPair:
                sumPair[backSum].append([array[i],array[k]])
            else:
                sumPair[backSum]=[[array[i],array[k]]]
    
    return numberList

array=[5, -5, -2, 2, 3, -3]
targetSum=0
print(fourNumberSum(array,targetSum))

