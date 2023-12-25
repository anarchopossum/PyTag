import os
import time

line_len = 54 

def prompt(location: str, text: str, options: dict[str,str]): 
    while 1 == 1:
        text_format(location, text)
        opt_format(options)

        # input management
        print()
        value = input("Type a letter option > ").lower()
        if value in options.keys():
            clear_screen()
            return(options.get(value))
        elif value == "q":
            clear_screen()
            exit()
        else:
            print("\033[F", end="")
            print("\033[F", end="")
            print(value, "is not a valid option")
            time.sleep(2.5)
            clear_screen()


def text_format(location:str, text: str):
    # Top Border: this will show the current location.
    # Subtract location name + 2 white spaces from total line len
    bar_amount = int(( line_len - len(location) - 2) / 2)
    # If title is even add an extra bar, else it's Gucci
    if bar_amount % 2 == 0:
        print("█" * bar_amount,f"{location}", "█" * bar_amount, end="█\n")
    else:
        print("█" * bar_amount,f"{location}", "█" * bar_amount)

    # print("█" * line_len)
    print(f"█  {' ':^48}  █")
    # line text formater
    words = text.split()
    temp_str = ''
    for value in words:
        if len(temp_str + value) + 1 <= 50:
            temp_str += value + " "
        else:
            print(f"█ {temp_str:<50} █")
            temp_str = value + " "
    print(f"█  {' ':^48}  █")
    print("█" * line_len)

def opt_format(options: dict):
    print(f"█  {' ':^48}  █")
    for key, selection in options.items():
        print(f"█ {key+') '+selection: <50} █")
    print(f"█  {' ':^48}  █")
    print("█" * line_len)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
