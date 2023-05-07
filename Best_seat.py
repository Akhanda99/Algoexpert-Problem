def bestSeat(seats):
    # Write your code here.
    count=0
    cList=[]
    flag=1
    pos=0
    max=0
    for i in range(0,len(seats)):
        if seats[i]==1:
            if flag==0:
                flag=1
                cList.append([pos,count])
                if count>max:
                    max= count
        else:
            if flag ==0:
                count+=1
            else:
                count=1
                flag=0
                pos=i
    if max==0:
        ans=-1
    else:
        for i in range(0,len(cList)):
            if cList[i][1]==max:
                if max%2==0:
                    ans=cList[i][0]+(max//2)-1
                    break
                else:
                    ans= cList[i][0]+(max//2)
                    break
        
    return ans
