from collections import defaultdict


strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
  res = defaultdict(list)
  for i in strs:
    res[tuple(sorted(i))].append(i)
  return res.values()