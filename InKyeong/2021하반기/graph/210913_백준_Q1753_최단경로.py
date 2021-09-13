import heapq
v, e = map(int, input().split())
k = int(input())

graph = {vertex : {} for vertex in range(1, v+1)}

for i in range(0, e) :
    a, b, c = map(int, input().split())
    graph[a][b] = c


def dijkstra(graph, start) :
    distances = { vertex : [float('inf'), start] for vertex in graph}

    distances[start] = [0, start]
    queue = []
    heapq.heappush(queue, [distances[start][0], start])

    while queue :
        current_distance, current_vertex = heapq.heappop(queue)
        if distances[current_vertex][0] < current_distance :
            continue
        for adj, weight in graph[current_vertex].items() :
            distance = current_distance + weight
            if distance < distances[adj][0] :
                distances[adj] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adj])

    for i in range(1, len(graph) + 1):
        if distances[i][0] == float('inf'):
            print('INF')
        else:
            print(distances[i][0])


    return distances

dijkstra(graph, k)