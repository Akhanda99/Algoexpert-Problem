

def spiralTraverse(array):
    # Write your code here.
    row=len(array)
    col=len(array[0])
    n=m=0
    x=min(row,col)
    r=row-1
    c=col
    sign=0
    ansList=[]
    for i in range(0,x):
        if sign==0:
            if i>0:
                m+=1
            for j in range(0,c):
                ansList.append(array[n][m])
                if j!=c-1:
                    m+=1
            n+=1
            for j in range(0,r):
                ansList.append(array[n][m])
                if j!=r-1:
                    n+=1
            sign=1
            c-=1
            r-=1
        
        else:
            m-=1
            for j in range(0,c):
                ansList.append(array[n][m])
                if j!=c-1:
                    m-=1
            n-=1
            for j in range(0,r):
                ansList.append(array[n][m])
                if j!=r-1:
                    n-=1
            sign=0
            c-=1
            r-=1
    print(ansList)
            

array=[
  [1, 2, 3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10, 9, 8, 7]
]
# array=[
#     [27, 12, 35, 26],
#     [25, 21, 94, 11],
#     [19, 96, 43, 56],
#     [55, 36, 10, 18],
#     [96, 83, 31, 94],
#     [93, 11, 90, 16]
#   ]
spiralTraverse(array)
