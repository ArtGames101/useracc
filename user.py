import sys, os, time

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def namereg(text="Enter Username"):
    clear_screen()
    print(text)
    choice = user_choice()
    try:
        os.makedirs("data")
    except:
        pass
    us = open("data/{}.py".format(choice), "w+")
    us.write("username = '{}'".format(choice))
    print("Saved Data!")
    us.close()

def passreg(text="Enter Password"):
    clear_screen()
    print(text)
    choice = user_choice()
    import os.path
    if os.path.isfile(text):
        input("Choose another password!")
        passreg(text=text)
    else:
        us = open("data/{}.py".format(choice), "w+")
        us.write("username = '{}'".format(choice))
        print("Saved Data!")
        us.close()
