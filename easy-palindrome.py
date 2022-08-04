import math
num = 82528

# first/my approach 
def isPalindrome(num) : 
  count = 0
  temp = num
  num2=0
  while(num > 0):
    if(count ==0):
      num2 += num % 10   
    else: 
      num2 = num2*10 + num % 10
    num = math.floor(num/10)
    count +=1
  return num2 == temp 
print(isPalindrome(num))

# some dude's approach
def isPalindrome(x) : 
  if(x < 0): 
    return False
  num = x
  reversed = 0
  while (x>0):
    reversed = reversed*10 + x % 10 
    x //= 10 
  return num == reversed 