text = input()
symbols_count = {}

for char in text:
    symbols_count[char] = symbols_count.get(char, 0) + 1

for char in sorted(symbols_count):
    print(f"{char}: {symbols_count[char]} time/s")
