def minRewards(scores):
    # Write your code here.
    reward=[1 for _ in range(len(scores))]
    for i in range(1,len(scores)):
        if scores[i]>scores[i-1]:
            reward[i]=reward[i-1]+1
        # print(reward)
    for j in reversed(range(len(scores)-1)):
        if scores[j]>scores[j+1]:
            reward[j]=max(reward[j],reward[j+1]+1)

    return sum(reward)

scores=[8, 4, 2, 1, 3, 6, 7, 9, 5]
print(minRewards(scores))
    
