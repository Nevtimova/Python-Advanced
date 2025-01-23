from collections import deque

substrings = deque(input().split())
main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}
required_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}
collected_colors = []

while substrings:
    first = substrings.popleft()
    last = substrings.pop() if substrings else ""

    color = first + last
    if color in main_colors or color in secondary_colors:
        collected_colors.append(color)
    else:
        first = first[:-1]
        last = last[:-1]
        if first:
            substrings.insert(len(substrings) // 2, first)
        if last:
            substrings.insert(len(substrings) // 2, last)

filtered_colors = [
    color for color in collected_colors if color in main_colors or
    all(req in collected_colors for req in required_colors.get(color, []))
]

print(filtered_colors)
