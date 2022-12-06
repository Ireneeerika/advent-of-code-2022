#!/usr/bin/env python3

import numpy as np
import re

def crates(f):
    stacks = {}
    linelist = []
    stacklist = []
    moveslist = []

    for line in f.splitlines():
        if line.startswith("[") or line.startswith("  "):
            linelist = []
            line = line.replace("    [", "X").replace(" [", "").replace("] ", "").replace("   ", "X").replace("[", "").replace("]", "").replace(" ", "")
            for char in line:
                linelist.append(char)
            stacklist.append(linelist)

        elif line.startswith("m"):
            moves = re.findall(r'[^\d]([\d]+)', line)
            moveslist.append(moves)
            
    arr = np.array(stacklist, dtype=object)
    
    for i in arr.T:
        stacks[len(stacks)+1] = (list(reversed(i)))
    
    for move in moveslist:
        how_many = int(move[0])
        from_stack = int(move[1])
        to_stack = int(move[2])
        
        holdlist = []
     
        for x in range(1, how_many+1):
            for i in reversed(range(len(stacks[from_stack]))):
                crate = stacks[from_stack][i]
                if crate == "X":
                    continue
                else:
                    holdlist.append(crate)
                    stacks[from_stack].pop(i)
                    stacks[from_stack].append("X")
                    break
        
        # For Part 1 comment next line
        holdlist.reverse()
        for y in holdlist:
            stacks[to_stack].append(y)

    resultlist = []
    for k, v in stacks.items():
        v = list(map(lambda x: x.replace('X', ''), v))
        v.reverse()
        for x in v:
            if x == "":
                continue
            else:
                resultlist.append(x)
                break
        
    return resultlist
        

with open('Advent/input_5.txt') as f:
    file = f.read()    
    order = crates(file)
    print("Top crates: ", order)
    
    
# Part 1 result:
# SPFMVDTZT
#
# Part 2 result:
# ZFSJBPRFP