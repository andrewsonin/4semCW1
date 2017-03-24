from heapq import heappush, heappop


def read(vxs, edges):
    graph = [[] for i in range(vxs)]
    for i in range(edges):
        t1, t2, w = tuple(map(int, input().split()))
        graph[t1].append((t2, w))
        graph[t2].append((t1, w))
    return graph


def dijkstra(graph, start, vertex_quantity, path_length):
    path_length[start] = (0, start)
    path_heap = []
    heappush(path_heap, (0, start))
    while path_heap:
        current = heappop(path_heap)[1]
        for neighbour in graph[current]:
            length = path_length[current][0] + neighbour[1]
            if length < path_length[neighbour[0]][0]:
                path_length[neighbour[0]] = length, start
                heappush(path_heap, (length, neighbour[0]))
    return path_length


main_towns = list(map(int, input().split()))
towns, roads, main_towns = main_towns[0], main_towns[1], main_towns[2:]
my_graph = read(towns, roads)
lengths = [(float('+inf'), -1)] * towns
for main_town in main_towns:
    dijkstra(my_graph, main_town, towns, lengths)
for elem in lengths:
    print(elem[1])
