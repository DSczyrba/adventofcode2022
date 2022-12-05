with open("input.txt") as f:
    data = f.read()
    data = [x for x in data.strip().split("\n")]
    data = [[x[:len(x)//2], x[len(x)//2:]] for x in data]

score = 0
for x in data:
    same_char = list(set(x[0]) & set(x[1]))[0]
    if same_char.isupper():
        value = ord(same_char) - 38
    else:
        value = ord(same_char) - 96
    score += value

print("Lösung 1:", score)

