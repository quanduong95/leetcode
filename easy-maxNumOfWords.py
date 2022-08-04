sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
def mostWordsFound(sentences):
  max = 0
  for i in sentences:
    count = i.count(' ')
    if count > max:
      max = count
  return max+1


print(mostWordsFound(sentences))