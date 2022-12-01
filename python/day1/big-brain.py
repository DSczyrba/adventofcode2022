with open("input.txt") as f:
    data = [[y for y in x.split("\n")] for x in f.read().split("\n\n")]

print(data)
