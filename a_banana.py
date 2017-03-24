hills_num = int(input())
graph = []
for i in range(hills_num):
    graph.append(list(map(int, input().split())))
input()
colors = list(map(int, input().split()))
bad_bridges = 0
for i in range(hills_num):
    for j in range(i, hills_num):
        if graph[i][j] == 1 and colors[i] != colors[j]:
            bad_bridges += 1
print(bad_bridges)
