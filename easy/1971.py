from collections import defaultdict
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
def validPath(edges,source,destination):
  graph = defaultdict(list)
  for i,k in edges:
    graph[i].append(k)
    graph[k].append(i)

  visited = set()
  queue = [source]
  visited.add(source)
  while queue != []:
    curr = queue.pop(0)
    if curr == destination :
      return True
    for neighbour in graph[curr]:
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append(neighbour)
  return False
    


  
