nums = [1,1,1,3,3,4,3,2,4,2]

def containsDuplicates(nums):
  set = set()
  for i in nums:
    if i not in set:
      set.add(i)
    else:
      return True
  return False


def containsDuplicates2(nums):
  set = set(nums)
  if(len(nums) > len(set)):
    return True
  return False