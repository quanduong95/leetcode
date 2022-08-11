class Node():
  def __init__(self,val):
    self.val = val
    self.next = None
class LinkedList():
  def __init__(self):
    self.head = None
  def printList(self,head):
    curr = head
    while curr is not  None:
      print(curr.val)
      curr=curr.next


list = LinkedList()
list.head = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
e6 = Node(6)

list.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
list.printList(Node(1))

def reverse(head):
  prev = None
  curr = head
  while curr:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  return prev

