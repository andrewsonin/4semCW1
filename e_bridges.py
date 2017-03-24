def count_iter(vertex_num, edge_num):
    graph = [[] for i in range(vertex_num)]
    for i in range(edge_num):
        used = set()
        v1, v2 = tuple(map(int, input().split()))
        graph[v1].append(v2)
        graph[v2].append(v1)
        dfs(v1, graph, used)
        if len(used) == vertex_num:
            return i + 1


def dfs(vertex, graph, used):
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)


v, e = tuple(map(int, input().split()))
print(count_iter(v, e))
