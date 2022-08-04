nums1 = [1,2,2,1]
nums2 = [2,3]

def intersection(nums1,nums2):
  res =[]
  for i in nums1:
    if i in nums2 and i not in res:
      res.append(i)
  return res
print(intersection(nums1,nums2))

def intersection2(nums1,nums2):
  res =dict()
  for i in nums1:
    if i in nums2 and i not in res:
      res[i] = i
  return list(res.keys())

def intersection3(nums1, nums2):
    return(list(set(nums1) & set(nums2)))