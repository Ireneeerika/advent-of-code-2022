#!/usr/bin/env python3

def calories():
    with open('/Advent/input_1.txt') as f:
        gnome = 0
        biggest_gnome = 0
        gnomelist =[]
        
        for line in f:            
            if line.strip():
                new = line.rstrip("\n")
                n = int(new)
                gnome += n
            else:
                gnomelist.append(gnome)
                if gnome > biggest_gnome:
                    biggest_gnome = gnome
                    gnome = 0
                else:
                    biggest_gnome = biggest_gnome
                    gnome = 0
                    
    return gnomelist
        
    
def biggest(gnomes):
    glist = sorted(gnomes, reverse=True)
    result = sum(glist[:3])
    best = glist[0]
    return (best, result)
          
result = calories()
best, top3 = biggest(result)

print(f"Most calories: {best}")
print(f"Three biggest carry: {top3}")