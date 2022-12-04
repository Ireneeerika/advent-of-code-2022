#!/usr/bin/env python3

def pairs(f):
    total = 0
    for line in f:
        p1, p2 = line.split(",")
        start_p1, end_p1 = p1.split("-")
        start_p2, end_p2 = p2.split("-")
        
        range1 = list(range(int(start_p1), int(end_p1)+1))
        range2 = list(range(int(start_p2), int(end_p2)+1))
        
        if range1 == []:
            range1 = [int(start_p1)]
        elif range2 == []:
            range2 = [int(start_p2)]
            
        #print(range1, range2)
        
        if all(i in range1 for i in range2):
            #print(f"{p1} included in {p2}")
            total += 1
            
        elif all(i in range2 for i in range1):
            #print(f"{p2} included in {p1}")
            total += 1
        
        elif range1 == range2:
            #print(f"{p1} is the same as {p2}")
            total += 1
        
        #else:
            #print(f"{p1} is different from {p2}")
    
    return total       


with open('/Users/irenejunttola/Documents/Python/Advent/advent-of-code-2022/input_4.txt') as f:
    file = f.readlines()
    result = pairs(file)
    #result2 = badges(file)
    print(f"Sum of the pairs: {result}")
    #print(f"Sum of the badges: {result2}")