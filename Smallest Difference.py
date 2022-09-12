def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    difList = []
    ansList = []
    for i in range(0, len(arrayOne)):
        for j in range(0, len(arrayTwo)):
            dif = abs(arrayOne[i] - arrayTwo[j])
            difList.append(dif)
            if min(difList) == difList[-1]:
                x = arrayOne[i]
                y = arrayTwo[j]
    ansList.append(x)
    ansList.append(y)
    return ansList



#Test 01
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
ans = smallestDifference(arrayOne, arrayTwo)
print(ans)