with open("input.txt") as f:
    data = f.read()
    data = [x for x in data.strip().split("\n")]
    data = [x.split() for x in data]

mapping = {"X": 0, "Y": 1, "Z": 2, "A": 0, "B": 1, "C": 2}

#      | X/0 | Y/1 | Z/2
# ----------------------
# A/0  | 3+1 | 6+2 | 0+3
# B/1  | 0+1 | 3+2 | 6+3
# C/2  | 6+1 | 0+2 | 3+3

scoring = [[3 + 1, 6 + 2, 0 + 3],
           [0 + 1, 3 + 2, 6 + 3],
           [6 + 1, 0 + 2, 3 + 3]]


values = [scoring[mapping[x[0]]][mapping[x[1]]] for x in data]

print("Lösung 1:", sum(values))
