from queue import Queue

f = open("inputs/day5.txt", "r")
lines = f.readlines()
f.close()

# build the stacks
line = lines.pop(0)
# You can actually find out the number of stacks judging by the number of whitespaces
stacks = [[] for _ in range(len(line) // 4)]
while line[1] != "1":
    for i in range(1, len(line), 4):
        if line[i] != " ":
            stacks[i // 4].append(line[i])
    line = lines.pop(0)

lines.pop(0)

# Reverse stacks: they were FIFO, now they should be LIFO
stacks = [stack[::-1] for stack in stacks]

# moving crates according to input
for line in lines:
    _, n_crates, _, from_stack, _, to_stack = line.rstrip().split(" ")

    for _ in range(int(n_crates)):
        stacks[int(to_stack) - 1].append(stacks[int(from_stack) - 1].pop())

top_crates = "".join([stacks[i][-1] for i in range(len(stacks))])
# join top crates in a string
print("".join(top_crates))