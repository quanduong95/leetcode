nums = [2, 7, 11, 15]
def twoSum(nums, target):
    # visited dictionary(map will store the number we passed )
    # visited will have form: value:index
    visited = {}
    count = 0
    for i in nums:
        if target-i in visited:
            return [count, visited[target-i]]
        else:
            visited[i] = count
        count += 1


















