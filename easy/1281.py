

n = 234
def subtractProductAndSum(n):
  s,p =0,1
  for k,v in enumerate(str(n)):
    s+=v
    p*=v
  return p-s