a = [1, 1, 1, 2, 2, 2, 3, 4, 5, 6, 6, 6, 8]
# my approach
def removeDup(a):
    count = 1
    while count < len(a):
        if(a[count] == a[count-1]):
            a.pop(count)
        else:
            count += 1
    return  count

print(removeDup(a))

# second attempt, fuck its way slower
def removeDup(a):
  for i in a:
    while(a.count(i) > 1):
      a.remove(i)
  return len(a)
print(removeDup(a))

# NeetCode's approach :
def removeDup(nums):
  count = 1
  for i in range(1,len(nums)):
    if(nums[i] != nums[i-1]):
      nums[count] = nums[i]
      count+=1
  return count