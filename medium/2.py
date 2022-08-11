class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def addTwoNumbers(l1,l2):
  mul =1
  sum1=sum2=0
  while l1 or l2:
    if l1:
      sum1+=l1.val*mul
      l1=l1.next
    if l2:
      sum2+=l2.val*mul
      l2=l2.next
    mul*=10
  sum = str(sum1+sum2)[::-1]
  
  dummy = ListNode()
  head = dummy
  
  for i in sum:
    head.next = ListNode(int(i))
    head=head.next
  return dummy.next