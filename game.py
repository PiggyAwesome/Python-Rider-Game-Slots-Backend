import os
import random
import time
from getpass import getpass
from tkinter.messagebox import showinfo


types = ["common", "rare", "epic"]

owned = []

common_chance = 50
rare_chance = 30
epic_chance = 20
coins = 2000
required_amount_for_spin = 200
new_spin_amount = 50
admin = True

common = ["Toyota RAV4", "Subaru Impreza", "Ford Explorer", "7 Toyota Corolla", "Ford Focus", "Chevrolet Impala", "Honda Civic", "Chevrolet Malibu"]
rare = ["Lancia Stratos", "Land Rover Defende", "Lamborghini Miura", "Mini", "Lotus Esprit", "Porsche 911", "Audi Quattro", "McLaren F1"]
epic = ["Lamborghini Veneno", "Koenigsegg CCXR Trevita", "Bugatti Divo", "Mercedes-Maybach Exeleo", "Bugatti Centodieci", "Bugatti La Voiture Noire", "Rolls-Royce Boat Tail"]

def get_new_item(typee, refund_coins, refund_required_amount_for_spin):
    global common, rare, epic

    marker = []
    if typee == "common":
        listy = common
    if typee == "rare":
        listy = rare
    if typee == "epic":
        listy = epic


    for x in listy:
        if x in owned:
            marker.append(x)

    if len(marker) == len(listy):
        print("\t\t" + "You already own all", typee, "cars! You have been refunded your coins.")
        return [refund_coins, refund_required_amount_for_spin]

    while True:
        item = random.choice(listy)
        if item in listy:
            owned.append(item)
            a2 = "a"
            if item[0] in "aeiou": a2 = "an"
            print("\t\t" + f"You got {a2} {item}")
            return 0


    


def buy_coins_popup(title="Buy Coins", message="\"Popup for buying coins.\""):
    showinfo(title, message)

def get_coins():
    global coins
    coins += int(input("Amount of coins: "))

def slots():
    global types, coins, required_amount_for_spin, new_spin_amount, epic_chance, rare_chance, common_chance
    
    old_coins = coins
    old_required_amount_for_spin = required_amount_for_spin
    print()

    randomint = random.randint(1, 100)
    
    if randomint <= common_chance:
        common = True
        selected = "common"
        stop = random.choice([1, 4, 7])
    
    elif randomint <= common_chance + rare_chance and randomint > common_chance:
        rare = True
        selected = "rare"
        stop = random.choice([2, 5, 8])
    
    
    elif randomint > common_chance + rare_chance:
        epic = True
        selected = "epic"
        stop = random.choice([3, 6, 9])
    if coins >= required_amount_for_spin:
        i = 0
        while True:
            for typee in types:
                i += 1
                print("\033[F" + "\t\t\t" + "          ")
                print("\033[F" + "\t\t\t" + typee)
                time.sleep(0.3)
                if i == stop:
                    coins -= required_amount_for_spin
                    required_amount_for_spin += new_spin_amount
                    a = "a"
                    if typee[0] in "aeiou": a = "an"
                    print("\t\t" + f"You got {a} {typee} car!")
                    return get_new_item(typee, old_coins, required_amount_for_spin)
    else:
        buy_coins_popup(title="Not enough coins!")
        return 0

while True:
    os.system("cls")
    number_select = 1
    print("\t\tMain Menu\t\t\n")
    print(f"\t\t[{number_select}] Get new car [{required_amount_for_spin}]\t\t")

    nOne = number_select
    number_select += 1
    if admin == True:
        print(f"\t\t[{number_select}] Get Coins [Free]\t\t")
        nTwo = number_select
        number_select += 1
    else:
        number_select += 0
        nTwo = 0
    print(f"\t\t[{number_select}] Buy Coins\t\t")

    nThree = number_select
    number_select += 1
    print(f"\t\t[{number_select}] Balance [{coins}]\t\t")

    nFour = number_select
    number_select += 1
    print(f"\t\t[{number_select}] Inventory\t\t")

    nFive = number_select
    number_select += 1
    print(f"\t\t[{number_select}] Quit\t\t")

    nSix = number_select
    number_select += 1

    
    quesnum = int(input(":: "))

    if quesnum == nOne:
        item_result = slots()
        if item_result != 0:
            coins = item_result[0]
            required_amount_for_spin = item_result[1]
            
        getpass("")
    
    elif quesnum == nTwo and admin == True:
        get_coins()

    elif quesnum == nThree:
        buy_coins_popup()
        getpass("")

    elif quesnum == nFour:
        print(coins)
        getpass("")

    elif quesnum == nFive:
        print("\n".join(owned))
        getpass("")

    elif quesnum == nSix:
        exit()
