
class Node():
  def __init__(self, val =None):
    self.val = val
    self.next = None
    
class LinkedList():
  def __init__(self):
    self.head = None
    
  def printList(self):
    data = self.head
    while data:
      print(data.val)
      data = data.next

list = LinkedList()
list.head = Node(1)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(3)

list.head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
list.printList()
print('break')
# 1 1 2 3 3 
def deleteDuplicates(head):
  if head is None:
    return head
  data = head
  while data:
    if data.next and data.next.val == data.val:
      data.next = data.next.next
    else:
      data=data.next
  return head
  #return the sorted linked list
deleteDuplicates(list.head)
list.printList()
  