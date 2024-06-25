# Tic Tac Toe in the terminal

import time

def win_check(coordinate_dict, player):
    x_list = []
    o_list = []
    if player == "p1":
        for coordinate in coordinate_dict.values():
            if coordinate.lower() == "x":
                x_list.append() # Here you need to append the dictionary key associated with the value that you just found out was X
                print(x_list)
        if ("a1", "a2", "a3") in x_list:
            print("Player 1 wins!")
            time.sleep(2)
            exit()
    

available_coordinates = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

coordinate_dict = {"a1": " ", "a2": " ", "a3": " ", "b1": " ", "b2": " ", "b3": " ", "c1": " ", "c2": " ", "c3": " "}

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
    while player_input not in available_coordinates:
        player_input = input("Not a valid input - place your cross or type \"quit\" to exit")
    if player_input.lower() == "quit":
        exit()
    #time.sleep(1)
    coordinate_dict[player_input.lower()] = "X"
    #time.sleep(1)

    #Win check for player
    win_check(coordinate_dict, "p1")
