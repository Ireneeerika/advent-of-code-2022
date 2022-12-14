#!/usr/bin/env python3


def rock_paper_scissors():
    opponent_points = 0
    player_points = 0
    
    with open('/Advent/input_2.txt') as f:
        for line in f:
            round = line.split()
            opponent, player = round
            
            if opponent == "A": #kivi
                if player == "X": #sakset #häviän
                    opponent_points += 7
                    player_points += 3
                elif player == "Y": #kivi #tasan
                    opponent_points += 4
                    player_points += 4
                elif player == "Z": #paperi #voitan
                    opponent_points += 2
                    player_points += 8
                     
            elif opponent == "B":
                if player == "X":
                    opponent_points += 8
                    player_points += 1
                elif player == "Y":
                    opponent_points += 5
                    player_points += 5
                elif player == "Z":
                    opponent_points += 2
                    player_points += 9
            
            elif opponent == "C":
                if player == "X":
                    opponent_points += 9
                    player_points += 2
                elif player == "Y":
                    opponent_points += 6
                    player_points += 6
                elif player == "Z":
                    opponent_points += 3
                    player_points += 7
                    
    return player_points
    
result = rock_paper_scissors()
print(f"My points: {result}")