with open("input.txt") as f:
    data = [[int(y) for y in x.split("\n")] for x in f.read().strip().split("\n\n")]
    data = sorted([sum(x) for x in data], reverse=True)


print(data)
print("Lösung 1:", data[0])
print("Lösung 2:", sum(data[:3]))

exit()

#Alternative:
data = sorted(
    (
        sum(int(y) for y in x.split("\n"))
        for x
        in f.read().strip().split("\n\n")
    ),
    reverse=True
)
