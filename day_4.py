#!/usr/bin/env python3

def pairs(f):
    # Part 1
    total = 0
    
    # Part 2
    overlapping = 0
    
    for line in f:
        p1, p2 = line.split(",")
        start_p1, end_p1 = p1.split("-")
        start_p2, end_p2 = p2.split("-")
        
        range1 = list(range(int(start_p1), int(end_p1)+1))
        range2 = list(range(int(start_p2), int(end_p2)+1))
        
        if not range1:
            range1 = int(start_p1)
        elif not range2:
            range2 = int(start_p2)
            
        if all(i in range1 for i in range2) or all(i in range2 for i in range1):
            total += 1
            overlapping += 1

        elif any(i in range1 for i in range2) or any(i in range2 for i in range1):
            overlapping += 1
         
    return total, overlapping


with open('/Users/irenejunttola/Documents/Python/Advent/advent-of-code-2022/input_4.txt') as f:
    file = f.readlines()
    total_pairs, overlapping = pairs(file)
    print(f"Sum of the pairs: {total_pairs}, overlapping: {overlapping}")