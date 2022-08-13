
def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s)-1,0,-1):
      s.append(s.pop(i))
    s.append(s.pop(0))