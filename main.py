# Tic Tac Toe in the terminal

import time
import random

#Initializing coordinates
coordinate_dict = {"a1": "X", "a2": "O", "a3": " ", "b1": "O", "b2": "X", "b3": " ", "c1": "O", "c2": " ", "c3": " "}

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
                print("\nYou have done it!")
                time.sleep(2)
                print("\nThrough your wily wits and incredible intelligence, you have bested me - entirely as expected.")
                time.sleep(3)
                print("\nI am overjoyed.")
                time.sleep(2)
                print("\nI shall retire - please do let me know if you wish to play again and it shall be my pleasure to do so!")
                time.sleep(5)
                exit()
        tie_check()
    if player == "p2":
        for key, value in coordinate_dict.items():
            if value.lower() == "o":
                o_list.append(key)
        for combination in win_combinations:
            if all(combo in o_list for combo in combination):
                current_playfield = update_playfield()
                time.sleep(5)
                print("\n...I cannot believe it.")
                time.sleep(3)
                print("\nBy way of some unfathomable prank of the universe, my circles have accidentally formed a line.")
                time.sleep(3)
                print("\nI am beyond distraught.")
                time.sleep(2)
                print("\nA thousand apologies, folded into a thousand more.")
                time.sleep(3)
                print("\nI shall retire - please do let me know if you wish to play again and it shall be my pleasure to do so.")
                time.sleep(3)
                print("\nNo expense will be spared in making sure this does not happen again.")
                time.sleep(3)
                print("\nUntil then, I bid you adieu.")
                time.sleep(5)
                exit()
        tie_check()
                
def tie_check():
    if " " not in coordinate_dict.values():
        current_playfield = update_playfield()
        time.sleep(4)
        print("\nIt appears that, somehow, we have arrived at a tie.")
        time.sleep(3)
        print("\nThis no doubt is due to some entirely random event, compelling me to place my circles in such a way as to block you from victory.")
        time.sleep(4)
        print("\nFrom the bottom of my robotic heart, I apologize.")
        time.sleep(3)
        print("\nDo let me know if you wish to play again, allowing me to correct this harrowing error.")
        time.sleep(5)
        exit()
        

def p1_play():
    player_input = input("Please select where to place your cross:\n\n")
    while player_input not in coordinate_dict.keys() and player_input != "quit":
        player_input = input("I must apologize, but that does not look to my humble eyes a valid input - write a coordinate (such as \"b2\") or \"quit\" to exit.\n\n")
    while coordinate_dict[player_input] != " ":
        time.sleep(1)
        player_input = input("\nMy deepest apologies, but it appears that square is already taken. Please choose another at your leisure.\n\n")
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
    —————————––––
    B {coordinate_dict["b1"]} | {coordinate_dict["b2"]} | {coordinate_dict["b3"]} |
    —————————––––
    C {coordinate_dict["c1"]} | {coordinate_dict["c2"]} | {coordinate_dict["c3"]} |
    """
    print(current_playfield)
    return current_playfield

def phrase_chooser():
    list_of_phrases = [
        "Excellent!",
        "Fantastic choice.",
        "Ah, ingenious.",
        "A wise move indeed.",
        "Well played."
    ]
    phrase = random.choice(list_of_phrases)
    return phrase

#Game initialization
print("\nHello dearest sir or madam! And welcome to your game of Tic, Tac and, as it were, Toe.")
time.sleep(3)
answer = input("\nWould it please the esteemed user to start the game? \n\n")
while not answer.lower() in ("yes", "yup", "yeah", "no", "nope", "nah"):
    time.sleep(1)
    answer = input("My deepest apologies, but I do not recognize that answer. Please reply with a single word, either an affirmative or a no, entirely at your leisure.\n\n")
if answer.lower() in ("no", "nope", "nah"):
    print("Very well. Feel free to call upon me again at any time!")
    time.sleep(3)
    exit()
if answer.lower() in ("yes", "yup", "yeah"):
    print("\nFantastic! Allow me to set it up.")
    time.sleep(2)
    current_playfield = update_playfield()
    time.sleep(2)
    print("\nI have taken the liberty of preparing this board.")
    time.sleep(2)
    print("\nMake your no doubt excellent selection by typing the corresponding coordinates - for example, a1, b2 or c3.")
    time.sleep(3)
    print("\nAnd with that - let's get started!")
    time.sleep(2)

#Core game loop
while True:    
    # Game loop
    current_playfield = update_playfield()
    time.sleep(2)
    p1_play()
    win_check("p1")
    current_playfield = update_playfield()
    time.sleep(2)
    phrase = phrase_chooser()
    print(phrase)
    time.sleep(2)
    print("\nI shall place a circle here: ")
    ai_play()
    time.sleep(2)
    win_check("p2")
    