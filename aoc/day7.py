from __future__ import annotations
from dataclasses import dataclass

# let's build a tree!
# first the data structures
@dataclass
class Node:
    name: str
    parent: Node

@dataclass
class File(Node):
    size: int

@dataclass
class Directory(Node):
    children: dict
    size: int = 0

# calculating sizes in post-order traversal, recursively
# I'm using post-order from the root here because I'm not sure if the last input is a leaf or not
total_sum = 0
def calculate_size(node):
    if isinstance(node, File):
        return node.size
    for child in node.children.values():
        node.size += calculate_size(child)
    if node.size <= 100000:
        global total_sum
        total_sum += node.size
    return node.size

def get_dir_to_delete(dir):
    global root_dir
    global curr_min
    if root_dir.size - dir.size < 40000000 and dir.size < curr_min:
        curr_min = dir.size
    for child in dir.children.values():
        if isinstance(child, Directory):
            get_dir_to_delete(child)

# now let's construct the actual tree from the input
f = open("inputs/day7.txt", "r")
lines = f.readlines()
f.close()

# ignore root cd
lines.pop(0)

# construct the tree
root_dir = Directory("/", None, {})
curr_dir = root_dir
for line in lines:
    if line[0] == "$":
        # ls can be ignored
        # it's possible to use just line[2:4] == "ls" (or, rahter, line[2] == "l"), but I'm leaving the redundant check in
        if line[2:4] == "ls":
            continue
        _, directory = line[2:].strip().split(' ')
        if directory == "..":
            curr_dir = curr_dir.parent
            continue
        # Try to find directory with name directory in curr_dir
        # If it doesn't exist, create it
        if directory not in curr_dir.children:
            curr_dir.children[directory] = Directory(directory, curr_dir, {})
        curr_dir = curr_dir.children[directory]
        continue

    # if it's not a cd command, it's a listing of either a file or a directory
    # in the current directory
    # since we don't know what it is yet, we'll call it fp, sp = first part, second part
    fp, sp = line.strip().split(' ')
    # if it's a directory
    if fp == "dir":
        if sp not in curr_dir.children:
            curr_dir.children[sp] = Directory(sp, curr_dir, {})
        continue
    # if it's a file
    fp = int(fp) # fp is the filesize
    if sp not in curr_dir.children:
        curr_dir.children[sp] = File(sp, curr_dir, fp)

calculate_size(root_dir)
print("Part one:", total_sum)

curr_min = root_dir.size
get_dir_to_delete(root_dir)
print("Part two:", curr_min)