# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    temp=head
    count=0
    while temp:
        count+=1
        temp= temp.next
    k= (count - k) + 1
    
    currentNode= head
    count=1
    if k==1:
        head.value= currentNode.next.value
        head.next= currentNode.next.next
            
    else:
        nextNode= currentNode.next
        while nextNode is not None:
            count+=1
            if count==k:
                currentNode.next= nextNode.next
            currentNode= currentNode.next
            nextNode= nextNode.next
    
