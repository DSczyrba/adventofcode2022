with open("input.txt") as f:
    data = f.readlines()
    data.append("\n")

highest = 0
current = 0
total = []

for x in data:
    try:
        current += int(x)
    except ValueError:
        if highest < current:
            highest = current
        current = 0

print(highest)