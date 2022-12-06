#!/usr/bin/env python3

import numpy as np

def start_of_packet(f):
    
    # Part 1: counter 4
    counter = 14
    # Part 1: charlist = [f[0], f[1], f[2]]
    charlist = [f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9], f[10], f[11], f[12]]
     
     # Part 1: f[13:]
    for char in f[13:]:
        charlist.append(char)
        x = np.array(charlist)
        
        # Part 1: == 4
        if len(np.unique(x)) == 14:
            return counter
        else:
            charlist.pop(0)
            counter += 1
            continue

with open('Advent/input_6.txt') as f:
    file = f.read()    
    result = start_of_packet(file)
    print(f"{result} characters.")