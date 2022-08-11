jewels = 'Bb'
stones ='aAAAAabbB'

def numJewelsInStones(jewels,stones):
  total = 0
  for i in jewels:
    total+= stones.count(i)
  return total

def numJewelsInStones2(jewels,stones):
  jset = set(jewels)
  counter = 0 
  for s in stones: 
      if s in jset:
          counter+=1
  return counter
