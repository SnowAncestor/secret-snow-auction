import Glave
import os
import platform
import Logo

def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')




def name():
    namesaver = input("What is your name: ")
    while True:
        bidsaver = input("What is your bid: ")
        if bidsaver.isdigit():  
            return namesaver, int(bidsaver)
        else:
            print("Please enter a valid number for your bid.")


def check_winner(names_list=None, bids_dict=None):
    if not names_list or not bids_dict:
        return "", 0

    name_of_winner = ""
    highest_bid = 0
    for name in names_list:
        bid = bids_dict.get(name, 0)  
        if bid > highest_bid:
            highest_bid = bid
            name_of_winner = name

    return name_of_winner, highest_bid

endAuction = True
dic = {}
names_list=[]
print("Welcome to the secret Snow auction!")

while endAuction:
    name_key, bid_value = name()
    if name_key=="":
        name_key="Unknown"
    if name_key not in dic:
        names_list.append(name_key)
    dic[name_key] = bid_value
    check = input("Are there any other bidders? press enter if yes or type 'no'. ").lower()
    if check == "no":
        endAuction = False
    else:
        clear_terminal()
        print(Glave.logo)
name_of_winner,bed=check_winner(names_list,dic)
clear_terminal()
print(Logo.logo)
print(f"The winner is {name_of_winner} with a bid of ${bed}.\n")
x=input("Press enter to finish ")
