prices = [2,9,16,3,6,14]

#sliding window (2 pointers) method:
def maxProfit (prices):
  l = 0
  r = 1
  profit=0
  while r < len(prices):
    if prices[r] > prices[l]:
      profit = max(profit,prices[r]-prices[l])
    else:
      l = r
    r+=1
  return profit
print(maxProfit(prices))