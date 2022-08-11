nums = [1, 3, 4, 2, 2]


# make nums[i] negative, if next time you see them negative that means DUP
def findDuplicate(nums):
    for i in nums:
        i = abs(i)
        if nums[i] < 0:
            return i
        else:
            nums[i] = -nums[i]


findDuplicate(nums)
