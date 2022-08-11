from collections import defaultdict
edges = [[1,2],[2,3],[4,2]]

def findCenter(self,edges):
  graph = defaultdict(list)
  for k,v in edges:
    graph[k].append(v)
    graph[v].append(k)
  for k in graph.keys():
    if len(graph[k])== len(graph)-1:
      return k
    
def findCenter2(edges):
  if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
    return edges[0][0]
  return edges[0][1]
