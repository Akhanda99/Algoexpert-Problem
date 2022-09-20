def moveElementToEnd(array, toMove):
    # Write your code here.
    for i in range(0, len(array)):
        if array[i] == toMove:
            array.remove(toMove)
            array.append(toMove)
        else:
            continue

    return array

#Test case -01
array=[2, 1, 2, 2, 2, 3, 4, 2]
toMove=2
print(moveElementToEnd(array,toMove))
