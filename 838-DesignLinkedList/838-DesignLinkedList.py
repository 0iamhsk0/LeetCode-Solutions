# Last updated: 11/1/2025, 9:33:26 PM
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        current = self.head
        cnt = 0
        while current is not None and cnt != index:
            current = current.next
            cnt += 1
        if current is None:
            return -1
        return current.val
        
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
            
        new_node = Node(val)
        ind = 0
        current = self.head
        while current is not None and ind != index - 1:
            current = current.next
            ind += 1
        if current is None:
            return
        new_node.next = current.next
        current.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        ind = 0
        current = self.head
        prev = None
        while current is not None and ind != index:
            prev = current
            current = current.next
            ind += 1
        if current is None:
            return
        prev.next = current.next
