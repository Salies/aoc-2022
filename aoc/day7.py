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
    # ls can be ignored
    # it's possible to use just line[2:4] == "ls" (or, rahter, line[2] == "l"), but I'm leaving the redundant check in
    if line[0] == "$":
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