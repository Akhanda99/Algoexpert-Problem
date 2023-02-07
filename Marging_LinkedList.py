# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    linkedListOne_set= set()
    currentNodeOne= linkedListOne
    currentNodeTwo= linkedListTwo

    while currentNodeOne:
        linkedListOne_set.add(currentNodeOne.value)
        currentNodeOne= currentNodeOne.next
    
    while currentNodeTwo:
        if currentNodeTwo.value in linkedListOne_set:
            return currentNodeTwo
        currentNodeTwo= currentNodeTwo.next

    return None