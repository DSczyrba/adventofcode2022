with open("input.txt") as f:
    data = f.read()
    data = [x for x in data.strip().split("\n")]
    data = [x.split() for x in data]

mapping = {"X": 0, "Y": 1, "Z": 2, "A": 0, "B": 1, "C": 2}

# Teil 1                   Teil 2        
#      | X/0 | Y/1 | Z/2   #      | X/0 | Y/1 | Z/2
# ----------------------   # ----------------------
# A/0  | 3+1 | 6+2 | 0+3   # A/0  | 0+3 | 3+1 | 6+2  Rock
# B/1  | 0+1 | 3+2 | 6+3   # B/1  | 0+1 | 3+2 | 6+3  Paper
# C/2  | 6+1 | 0+2 | 3+3   # C/2  | 0+2 | 3+3 | 6+1  Scissor

scoring1 = [[3 + 1, 6 + 2, 0 + 3],
            [0 + 1, 3 + 2, 6 + 3],
            [6 + 1, 0 + 2, 3 + 3]]

scoring2 = [[0 + 3, 3 + 1, 6 + 2],
            [0 + 1, 3 + 2, 6 + 3],
            [0 + 2, 3 + 3, 6 + 1]]

values1 = [scoring1[mapping[x[0]]][mapping[x[1]]] for x in data]
values2 = [scoring2[mapping[x[0]]][mapping[x[1]]] for x in data]

print("Lösung 1:", sum(values1))
print("Lösung 2:", sum(values2))