def bestDigits(number, numDigits):
    # Write your code here.
    numberList=[]
    large_num=-9999
    count=0
    
    for i in range(0,len(number)):
        if int(large_num)==0 and count<numDigits:
            numberList.pop()
            large_num=numberList[-1]
            count+=1
           
        if int(large_num)<=int(number[i]) and len(numberList)!=0 and count<numDigits:
            numberList.pop()
            count+=1
        
        if number[i]!=0:
            large_num= number[i] 
        numberList.append(number[i])
        
    if count<numDigits:
        for i in range(0,numDigits):
            numberList.pop()

    return ''.join(numberList)

number = "462839"
numDigits = 2
result = bestDigits(number, numDigits)
print(result)