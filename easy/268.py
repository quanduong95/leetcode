nums = [9,6,4,2,3,5,7,0,1]
#[0,1,3,4]
def missingNum(nums):
  nums = sorted(nums)

  for i in range(len(nums)-1):
      if nums[i+1] != nums[i]+1:
        return i+1
  if nums[0] == 1:
      return 0
  return len(nums)
print(missingNum(nums))


def missingNumber2(nums):
  res = len(nums)
  for i in range(len(nums)):
    res += (i - nums[i])
  return res