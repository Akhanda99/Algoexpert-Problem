class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
    p1= None
    p2= head

    while p2 is not None:
        p3= p2.next
        p2.next=p1
        
        p1=p2
        p2=p3
    return p1
    
