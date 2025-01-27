matrix = [input().split() for _ in range(5)]

player_row, player_col = 0, 0
for row in range(5):
    if "A" in matrix[row]:
        player_row, player_col = row, matrix[row].index("A")
        break

n = int(input())

targets_hit = []
total_targets = sum(row.count("x") for row in matrix)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for _ in range(n):
    command = input().split()
    action = command[0]
    direction = command[1]
    dr, dc = directions[direction]

    if action == "move":
        steps = int(command[2])
        for _ in range(steps):
            new_row, new_col = player_row + dr, player_col + dc
            if 0 <= new_row < 5 and 0 <= new_col < 5 and matrix[new_row][new_col] == ".":
                player_row, player_col = new_row, new_col
            else:
                break
    elif action == "shoot":
        shot_row, shot_col = player_row, player_col
        while 0 <= shot_row + dr < 5 and 0 <= shot_col + dc < 5:
            shot_row += dr
            shot_col += dc
            if matrix[shot_row][shot_col] == "x":
                matrix[shot_row][shot_col] = "."
                targets_hit.append([shot_row, shot_col])
                break

        if len(targets_hit) == total_targets:
            print(f"Training completed! All {total_targets} targets hit.")
            break
else:
    print(f"Training not completed! {total_targets - len(targets_hit)} targets left.")

for target in targets_hit:
    print(target)
