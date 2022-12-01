with open("input.txt") as f:
    data = f.readlines()
    data.append("\n")

current = 0
werte = []

for x in data:
    try:
        current += int(x)
    except ValueError:
        werte.append(current)
        current = 0

werte.sort(reverse=True)
print(sum(werte[:3]))