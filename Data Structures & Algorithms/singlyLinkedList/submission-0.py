class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1  # Index out of bounds     

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        
        # If list was empty, update tail
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next  # Move tail forward

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        
        # Move to node BEFORE the one to remove
        while i < index and curr.next:
            i += 1
            curr = curr.next
        
        # Check if index is valid
        if curr.next:
            # If removing tail, update tail pointer
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        values = []
        curr = self.head.next  # Skip dummy
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values
