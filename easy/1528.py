#not optimized yet
def suffleString(str,indices):
  res = ['' for i in range(len(indices))]
  for i,v in enumerate(indices):
    res[v] = str[i]
  return ''.join(res)