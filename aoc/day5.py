from copy import deepcopy

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
# alternatives you could use a deque or pop(0)
stacks = [stack[::-1] for stack in stacks]
# deepcopy the stacks for part 2
aux_stacks = deepcopy(stacks)

# moving crates according to input
for line in lines:
    _, n_crates, _, from_stack, _, to_stack = line.rstrip().split(" ")

    for _ in range(int(n_crates)):
        stacks[int(to_stack) - 1].append(stacks[int(from_stack) - 1].pop())

top_crates = "".join([stacks[i][-1] for i in range(len(stacks))])
# join top crates in a string
print("Part one: " + "".join(top_crates))

# Part 2
stacks = aux_stacks
for line in lines:
    _, n_crates, _, from_stack, _, to_stack = line.rstrip().split(" ")

    # Not much changes but the index of the popped element
    n_crates = int(n_crates)
    diff = len(stacks[int(from_stack) - 1]) - n_crates
    for _ in range(n_crates):
        stacks[int(to_stack) - 1].append(stacks[int(from_stack) - 1].pop(diff))

top_crates = "".join([stacks[i][-1] for i in range(len(stacks))])
print("Part two: " + "".join(top_crates))

# Note: in Python, I'm pretty sure it would be more efficient to move multiple elements at once
# instead of using pop. But I wanted to solve this problem purely based on data structure principles.