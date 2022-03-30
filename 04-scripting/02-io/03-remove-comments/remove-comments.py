import sys

with open(sys.argv[1]) as f:
        lines = f.readlines()

new_lines = []
for line in lines:
    if '#' in line:
        line = line[:line.index('#')]
    new_lines.append(line)

with open(sys.argv[1], 'w') as f:
    f.writelines(new_lines)		