s ="]"

# first approach
def isValid(s):
  stack = []
  keys = ['{','(','[']
  for i in s:
    if(i in keys):
      stack.append(i)
    elif(i == '}' and len(stack) !=0 and stack[len(stack)-1] == '{'):
      stack.pop()
    elif(i == ')' and len(stack) !=0 and stack[len(stack)-1] == '('):
      stack.pop()
    elif(i == ']' and len(stack) !=0 and stack[len(stack)-1] == '['):
      stack.pop() 
    else:
      return False    
  return len(stack)==0 

# second approach
def isValid2(s):
  stack = []
  list = ['{','(','[']
  comb = {
    ')':'(',
    '}':'{',
    ']':'[',
    
  } 
  for i in s:
    if(i in comb):  
      if(stack and stack[-1] == comb[i]):
        stack.pop()
      else:
        return False
    else:
      stack.append(i)
  return len(stack)== 0
