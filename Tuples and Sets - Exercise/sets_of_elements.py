n, m = map(int, input().split())
set1 = {int(input()) for _ in range(n)}
set2 = {int(input()) for _ in range(m)}
common_elements = set1.intersection(set2)
print("\n".join(map(str, common_elements)))
