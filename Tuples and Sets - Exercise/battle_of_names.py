n = int(input())
odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name = input()
    ascii_sum = sum(ord(char) for char in name) // i

    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum)
    else:
        odd_set.add(ascii_sum)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    result = odd_set.union(even_set)
elif odd_sum > even_sum:
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)

print(", ".join(map(str, result)))
