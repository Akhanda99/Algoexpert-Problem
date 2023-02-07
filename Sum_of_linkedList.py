# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    linkedListHeadPointer= LinkedList(0)
    currentNode= linkedListHeadPointer
    carry=0

    nodeofOne= linkedListOne
    nodeofTwo= linkedListTwo

    while nodeofOne is not None or nodeofTwo is not None or carry != 0:
        valueofNodeOne= nodeofOne.value if nodeofOne is not None else 0
        valueofNodeTwo = nodeofTwo.value if nodeofTwo is not None else 0
        sumofNodes= valueofNodeOne + valueofNodeTwo + carry

        newvalue= sumofNodes % 10
        carry= sumofNodes // 10
        
        newNode= LinkedList(newvalue)
        currentNode.next= newNode

        currentNode= newNode
        nodeofOne= nodeofOne.next if nodeofOne is not None else None
        nodeofTwo = nodeofTwo.next if nodeofTwo is not None else None

    

    return linkedListHeadPointer.next