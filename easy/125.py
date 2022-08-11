s = "A man, a plan, a canal: Panama"
def isPalindrome(s):
  s = ''.join(e.lower() for e in s if e.isalnum())
  s2 = s[::-1]
  return s==s2