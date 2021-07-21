# Using a Python dictionary to act as an adjacency list
# graph = {

#   's' : ['r','w'],
#   'r' : ['s', 'v'],
#   'w' : ['s', 'x', 't'],
#   'v' : ['r'],
#   'x' : ['w', 'y', 't'],
#   't' : ['w', 'x', 'u'],
#   'y' : ['x', 'u'],
#   'u' : ['x', 't', 'y']
# }
graph = {

  's' : set(['r','w']),
  'r' : set(['s', 'v']),
  'w' : set(['s', 'x', 't']),
  'v' : set(['r']),
  'x' : set(['w', 'y', 't']),
  't' : set(['w', 'x', 'u']),
  'y' : set(['x', 'u']),
  'u' : set(['x', 't', 'y'])
}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

dfs(graph, 's')

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
vertax = ['s', 'r', 't', 'u', 'v','w', 'x', 'y']
d = []
pi = []
for i in range(0, len(vertax)):               
    li = list(dfs_paths(graph, 's', vertax[i]))
    if len(li) == 0:
        d.append(0)
        pi.append('None')
    elif i == len(vertax)-2:
        d.append(len(li[2]) - 1)
        pi.append(li[2][len(li[2])-2])
    elif i == len(vertax)-1:
        d.append(len(li[1]) - 1)
        pi.append(li[1][len(li[1])-2])
    else :
        d.append(len(li[0]) - 1)
        pi.append(li[0][len(li[0])-2])
    
for i in range(0, len(vertax)):
    print("vertax ", vertax[i], "| d ", d[i], "| pi ", pi[i])


    