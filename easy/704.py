def binarySearch(nums,target):
  low = 0
  high = len(nums)
  while low <= high:
    mid = low + ((high - low) // 2)
    if nums[mid] == target:
      return mid
    elif nums[mid]> target:
      high = mid-1
    else:
      low = mid+1
  return -1