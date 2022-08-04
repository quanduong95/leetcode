s = 'MCMXCIV'
def romanToInt(s):
  table = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
  res = table[s[len(s)-1]]
  for count in range(len(s)-2,-1,-1):
    if(table[s[count]]>=table[s[count+1]]):
        res+= table[s[count]]
    else:
        res-=table[s[count]]
  return res

print(romanToInt('IXC'))