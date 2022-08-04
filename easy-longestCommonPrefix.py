strs = ["flower","flow","flight"]

def longestCommonPrefix(strs):
  res = ''
  for count in range(len(strs[0])):
    for i in strs:
      if count == len(i) or i[count] != strs[0][count]:
        return res
    res+=strs[0][count]
  return res