with open("input.txt") as f:
    data = f.read()

tower = []
command = []
for x in data.split("\n"):
    if "move" in x:
        command.append(x)
    else:
        tower.append(x)

t = []
for i in tower:
    print(i)