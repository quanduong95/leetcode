from collections import Counter, defaultdict

s = "anagram"
t = "nagaram"
def isAnagram(self, s: str, t: str) -> bool:
  return Counter(s) == Counter(t)
def isAnagram2(s,t):
  if len(s) != len(t):
    return False
  counter = defaultdict(int)
  for i in range(len(s)):
    counter[s[i]]+=1
    counter[t[i]]-=1
  for k,v in counter.items():
    if v!=0:
      return False
  return True