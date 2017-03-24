def read(vxs, edges):
    graph = [[] for i in range(vxs)]
    for i in range(edges):
        t1, t2 = tuple(map(int, input().split()))
        graph[t1].append(t2)
        graph[t2].append(t1)
    return graph


def is_bipart(graph, start, evens, odds, used, not_used, even=True):
    if even:
        evens.add(start)
    else:
        odds.add(start)
    used.add(start)
    not_used.discard(start)
    for neighbour in graph[start]:
        if neighbour not in used:
            if not is_bipart(graph, neighbour, evens, odds, used, not_used, even ^ True):
                return False
        elif neighbour in evens:
            if even:
                return False
        elif not even:
            return False
    return True

v, e = tuple(map(int, input().split()))
my_graph = read(v, e)
not_used_set = {i for i in range(v)}
even_set, odd_set, used_set = set(), set(), set()
is_no = False
while not_used_set:
    if not is_bipart(my_graph, not_used_set.pop(), even_set, odd_set, used_set, not_used_set):
        is_no = True
        break
if is_no:
    print('NO')
else:
    print(' '.join(map(str, even_set)))
