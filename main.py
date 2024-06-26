# Tic Tac Toe in the terminal

import time

coordinate_dict = {"a1": " ", "a2": " ", "a3": " ", "b1": " ", "b2": " ", "b3": " ", "c1": " ", "c2": " ", "c3": " "}

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

def win_check(coordinate_dict, player):
    x_list = []
    o_list = []
    if player == "p1":
        for key, value in coordinate_dict.items():
            if value.lower() == "x":
                x_list.append(key)
        for combination in win_combinations:
            if combination[0] and combination[1] and combination[2] in x_list:
                print(current_playfield)
                time.sleep(1)
                print("Player 1 wins!")
                time.sleep(3)
                exit()

while True:
    #Update playfield
    current_playfield = f"""
      1   2   3
    A {coordinate_dict["a1"]} | {coordinate_dict["a2"]} | {coordinate_dict["a3"]} |
    —————————–––
    B {coordinate_dict["b1"]} | {coordinate_dict["b2"]} | {coordinate_dict["b3"]} |
    —————————–––
    C {coordinate_dict["c1"]} | {coordinate_dict["c2"]} | {coordinate_dict["c3"]} |
    """
    print(current_playfield)
    #Player input
    player_input = input("Place your cross: ")
    while player_input not in coordinate_dict.keys():
        player_input = input("Not a valid input - place your cross or type \"quit\" to exit")
    if player_input.lower() == "quit":
        exit()
    coordinate_dict[player_input.lower()] = "X"
    #Win check for player
    win_check(coordinate_dict, "p1")
