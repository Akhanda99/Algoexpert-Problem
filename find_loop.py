# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # Write your code here.
    firstNode= head.next
    secondNode= head.next.next
    while firstNode != secondNode:
        firstNode= firstNode.next
        secondNode= secondNode.next.next

    firstNode=head
    while firstNode!= secondNode:
        firstNode= firstNode.next
        secondNode= secondNode.next

    return firstNode
            
            