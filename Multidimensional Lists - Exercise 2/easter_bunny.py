n = int(input())

field = []
bunny_row, bunny_col = 0, 0

for row in range(n):
    line = input().split()
    field.append(line)
    if "B" in line:
        bunny_row, bunny_col = row, line.index("B")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

best_direction = ""
best_path = []
max_eggs = -999999999

for direction, (dr, dc) in directions.items():
    row, col = bunny_row, bunny_col
    eggs = 0
    path = []

    while 0 <= row + dr < n and 0 <= col + dc < n:
        row += dr
        col += dc

        if field[row][col] == "X":
            break

        eggs += int(field[row][col])
        path.append([row, col])

    if eggs > max_eggs:
        max_eggs = eggs
        best_direction = direction
        best_path = path

print(best_direction)
for pos in best_path:
    print(pos)
print(max_eggs)
