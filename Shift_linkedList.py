# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    # Write your code here.
    
    if k>=0:
        temp=head
        for i in range(0,k):
            while temp.next!=None:
                temp2=temp
                temp=temp.next
            temp2.next=None
            temp.next=head
            head= temp

    elif k<0:
        k=abs(k)
        temp=head
        for i in range(0,k):
            firstNode=head
            while temp.next!=None:
                temp=temp.next
            head= firstNode.next
            temp.next=firstNode
            firstNode.next=None
    
    return head