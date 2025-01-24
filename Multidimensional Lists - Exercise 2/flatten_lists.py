data = input()

result = [int(num) for sublist in data.split('|')[::-1] for num in sublist.split() if num]

print(*result)
