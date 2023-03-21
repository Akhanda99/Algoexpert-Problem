class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    ll1=headOne
    ll2=headTwo
    margedLL=LinkedList(0)
    currentNode=margedLL

    while ll1 is not None or ll2 is not None:
        val1=ll1.value if ll1 is not None else 9999
        val2=ll2.value if ll2 is not None else 9999
        if val1<val2:
            newNode=LinkedList(val1)
            ll1=ll1.next
        else:
            newNode=LinkedList(val2)
            ll2=ll2.next

        currentNode.next=newNode
        currentNode=currentNode.next


    return margedLL.next
    
