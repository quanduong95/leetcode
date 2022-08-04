nums = [4,1,2,1,2]

def singleNum(nums):
  store = dict()
  for i in nums:
    if i in store:
      store[i] = 2
    else:
      store[i] = 1
  for k,v in store.items():
    if v == 1:
      return k
print(singleNum(nums))