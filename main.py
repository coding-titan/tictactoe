# Tic Tac Toe in the terminal

import time
import random

#Initializing coordinates
coordinate_dict = {"a1": " ", "a2": " ", "a3": " ", "b1": " ", "b2": " ", "b3": " ", "c1": " ", "c2": " ", "c3": " "}

#List of combinations leading to win
win_combinations = [
    ("a1", "a2", "a3"),
    ("b1", "b2", "b3"),
    ("c1", "c2", "c3"),
    ("a1", "b1", "c1"),
    ("a2", "b2", "c2"),
    ("a3", "b3", "c3"),
    ("a1", "b2", "c3"),
    ("a3", "b2", "c1")
]

#Functions
def win_check(player):
    x_list = []
    o_list = []
    if player == "p1":
        for key, value in coordinate_dict.items():
            if value.lower() == "x":
                x_list.append(key)
        for combination in win_combinations:
            if all(combo in x_list for combo in combination):
                current_playfield = update_playfield()
                time.sleep(1)
                print("Player 1 wins!")
                time.sleep(3)
                exit()
    if player == "p2":
        for key, value in coordinate_dict.items():
            if value.lower() == "o":
                o_list.append(key)
        for combination in win_combinations:
            if all(combo in o_list for combo in combination):
                current_playfield = update_playfield()
                time.sleep(1)
                print("Computer wins!")
                time.sleep(3)
                exit()
                
def p1_play():
    player_input = input("Place your cross: ")
    while player_input not in coordinate_dict.keys():
        player_input = input("Not a valid input - place your cross or type \"quit\" to exit")
    if player_input.lower() == "quit":
        exit()
    coordinate_dict[player_input.lower()] = "X"

def ai_play():
    avaiable_coordinates = []
    for key, value in coordinate_dict.items():
        if not value == "X" and not value == "O":
            avaiable_coordinates.append(key)
    choice = random.choice(avaiable_coordinates)
    coordinate_dict[choice] = "O"
    
def update_playfield():
    current_playfield = f"""
      1   2   3
    A {coordinate_dict["a1"]} | {coordinate_dict["a2"]} | {coordinate_dict["a3"]} |
    —————————–––
    B {coordinate_dict["b1"]} | {coordinate_dict["b2"]} | {coordinate_dict["b3"]} |
    —————————–––
    C {coordinate_dict["c1"]} | {coordinate_dict["c2"]} | {coordinate_dict["c3"]} |
    """
    print(current_playfield)
    return current_playfield

#Core game loop
while True:
    current_playfield = update_playfield()
    p1_play()
    win_check("p1")
    current_playfield = update_playfield()
    ai_play()
    win_check("p2")
    current_playfield = update_playfield()
    