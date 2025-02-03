import os
import re


def even_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i in range(0, len(lines), 2):
        line = lines[i]
        line = re.sub(r'[-,\.!?]', '@', line)
        words = line.split()[::-1]
        print(' '.join(words))


def line_numbers(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for i, line in enumerate(infile, 1):
            letters = sum(c.isalnum() for c in line)
            punctuation = sum(1 for c in line if not c.isalnum() and not c.isspace())
            outfile.write(f"Line {i}: {line.strip()} ({letters})({punctuation})\n")


def file_manipulator():
    while True:
        command = input()
        if command == "End":
            break
        parts = command.split('-')
        action, filename = parts[0], parts[1]

        if action == "Create":
            open(filename, 'w').close()
        elif action == "Add":
            content = parts[2]
            with open(filename, 'a') as file:
                file.write(content + '\n')
        elif action == "Replace":
            if not os.path.exists(filename):
                print("An error occurred")
                continue
            old, new = parts[2], parts[3]
            with open(filename, 'r') as file:
                content = file.read().replace(old, new)
            with open(filename, 'w') as file:
                file.write(content)
        elif action == "Delete":
            if os.path.exists(filename):
                os.remove(filename)
            else:
                print("An error occurred")


def directory_traversal(directory):
    report = {}
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            ext = os.path.splitext(item)[1]
            report.setdefault(ext, []).append(item)

    with open(os.path.join(directory, 'report.txt'), 'w') as report_file:
        for ext in sorted(report.keys()):
            report_file.write(f"{ext}\n")
            for file in sorted(report[ext]):
                report_file.write(f" - {file}\n")

# Example usage
# even_lines("text.txt")
# line_numbers("text.txt", "output.txt")
# file_manipulator()
# directory_traversal(".")
