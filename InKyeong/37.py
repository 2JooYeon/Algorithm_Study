vartex = ['s', 't', 'y', 'x', 'z']
graph = [[0, 3, 5, 0, 0], 
        [0, 2, 0, 6, 0],
        [0, 1, 0, 4, 6],
        [0, 0, 0, 0, 2],
        [3, 0, 0, 7, 0]]

def path(tovartex, parent, id) :
    var = vartex[id]
    if parent[id] == -1 :
        print(var, end='->')
        return
    path(tovartex, parent, parent[id])
    if(var != tovartex) :
        print(var, end='->')
    else :
        print(var)

def compute_min_dist(dist, q):
    index = -1
    INF = float("inf")
    for i in range(len(dist)):
        if dist[i] < INF and i in q:
            INF = dist[i]
            index = i
    return index

def dijkstra(graph, source) :
    source = vartex.index(source)

    distance = [float("Inf")] * len(graph)
    distance[source] = 0

    path = [-1] * len(graph)
    q = []

    for i in range(0, len(graph)) :
        q.append(i)
    while q :
        m = compute_min_dist(distance, q)
        q.remove(m)

        for i in range(0, len(graph)):
            if i in q and graph[m][i] :
                if distance[i] > distance[m] + graph[m][i] :
                    distance[i] = distance[m] + graph[m][i]
                    path[i] = m

    return distance, path

d, p = dijkstra(graph, 's')
idx = vartex.index('y')
print('s to y | cost ', d[idx], '| path ', end='')
path('y',p, idx)

idx = vartex.index('z')
print('s to z | cost ', d[idx], '| path ', end='')
path('z',p, idx)

