alphabet = dict(enumerate(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')))
rev_alphabet = {letter: i for i, letter in alphabet.items()}
reverse = lambda x: (rev_alphabet[x[0]], int(x[1]) - 1)
start = reverse(input())
end = reverse(input())

coord_changes = ((1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1))
path = {start: [start]}
queue = [start]
while queue:
    current = queue.pop(0)
    for change_x, change_y in coord_changes:
        cur_x, cur_y = current
        cur_x += change_x
        cur_y += change_y
        neighbour = cur_x, cur_y
        if 0 <= cur_x <= 7 and 0 <= cur_y <= 7 and neighbour not in path:
            queue.append(neighbour)
            path[neighbour] = path[current] + [neighbour]
        if neighbour == end:
            queue = []
for elem in path[end]:
    print(alphabet[elem[0]] + str(elem[1] + 1))
