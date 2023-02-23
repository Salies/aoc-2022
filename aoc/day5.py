from queue import Queue

f = open("inputs/day5.txt", "r")
lines = f.readlines()
f.close()

# build the stacks
line = lines.pop(0)
# You can actually find out the number of stacks judging by the number of whitespaces
stacks = [Queue() for i in range(len(line) // 4)]
while line[1] != "1":
    for i in range(1, len(line), 4):
        if line[i] != " ":
            stacks[i // 4].put(line[i])
    line = lines.pop(0)

lines.pop(0)

# moving crates according to input
for line in lines:
    _, n_crates, _, from_crate, _, to_crate = line.rstrip().split(" ")

    for i in range(int(n_crates)):
        stacks[int(to_crate) - 1].put(stacks[int(from_crate) - 1].get())