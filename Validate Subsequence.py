def isValidSubsequence(array, sequence):
    # Write your code here.
    count=0
    seq=0
    for i in range(0,len(array)):
        if array[i] in sequence:
            if seq<len(sequence):
                if sequence[seq]==array[i]:
                    count+=1
                    seq+=1
        else:
            continue
    
    return count==len(sequence)


#test case 1
array=[5, 1, 22, 25, 6, -1, 8, 10]
sequence= [1, 6, -1, 5]
print(isValidSubsequence(array,sequence))

#test case 2
array1= [5, 1, 22, 25, 6, -1, 8, 10]
sequence1=[5, -1, 8, 10]
print(isValidSubsequence(array1,sequence1))