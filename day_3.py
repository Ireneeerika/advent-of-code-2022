#!/usr/bin/env python3

lower = dict(zip("a b c d e f g h i j k l m n o p q r s t u v w x y z".split(), 
                 range(1,27)))
upper = dict(zip("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(), 
                 range(27,53)))

def rucksack(f):
    total = 0
    for line in f:
        h1 = slice(0, len(line)//2)
        h2 = slice(len(line)//2, len(line))
            
        letter = [x for x in line[h1] if x in line[h2]][0]
            
        if letter in lower.keys():
            total += lower[letter]
        elif letter in upper.keys():
            total += upper[letter]
    
    return total       

def badges(f):
    
    total_group = 0
    counter = 0
    linelist = []
    total_list = []

    for line in f:
        linelist.append(line.strip())
        counter += 1
        if counter == 3:
            total_list.append(linelist)
            linelist = []
            counter = 0
    
    for i in total_list:  
        letter = [x for x in i[0] if x in i[1] and x in i[2]][0]       
        if letter in lower.keys():
            total_group += lower[letter]
        elif letter in upper.keys():
            total_group += upper[letter]
               
    return total_group

    
with open('Advent/input_3.txt') as f:
    file = f.readlines()
    result = rucksack(file)
    result2 = badges(file)
    print(f"Sum of the priorities: {result}")
    print(f"Sum of the badges: {result2}")