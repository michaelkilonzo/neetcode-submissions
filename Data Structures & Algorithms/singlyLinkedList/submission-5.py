class ListNode:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(float("-inf"))
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0 
        while curr:
            if i == index:
                return curr.val
            i += 1  
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode

        if self.tail == self.head:
            self.tail = newNode 

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)

        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        prev = self.head 
        i = 0 

        while i < index and prev.next:
            i += 1
            prev = prev.next
        
        if not prev.next:
            return False

        if prev.next == self.tail:
            self.tail = prev
            self.tail.next = None  # unlink the old tail
        else:
            prev.next = prev.next.next
        return True

    def getValues(self) -> List[int]:
        vals = []
        curr = self.head.next 

        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        return vals
