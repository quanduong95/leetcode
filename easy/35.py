nums = [1,2,5,6]
target = 4

def searchInsert(nums,target):
  count = 0
  while count < len(nums):
    if(target < nums[0]):
      return 0 
    if(target > nums[count]):
      if(count == len(nums) -1):
        return len(nums)
      else:
        count+=1
    else:
      return count
        

print(searchInsert(nums,target))
  
def searchInsert2( nums, target):
    low = 0
    high = len(nums)-1
    while(low<=high):
        mid = (high+low)//2
        guess = nums[mid]
        if(target == guess):
            return mid
        elif(target>guess):
            low = mid +1
        else: 
            high = mid-1
    return low

searchInsert2(nums,target)
