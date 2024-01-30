import os
import time

line_len = 54


class location():
    def __init__(self, loc_data: dict) -> None:
        self.title = loc_data['title_screen']['title']


def prompt(location_title: str, prompt_text: str, options: tuple): 
    while 1 == 1:
        text_format(location_title, prompt_text)
        formatted_options = opt_format(options)

        # input management
        print()
        selection = input("Type a letter option > ").lower()
        if selection in formatted_options.keys():
            clear_screen()
            # Debug print(formatted_options[selection][1])
            return formatted_options[selection][1]
        elif selection == "q":
            clear_screen()
            exit()
        else:
            print("\033[F", end="")
            print("\033[F", end="")
            print(selection, "is not a valid option")
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
    # if the current temp string + the next word is <= 50 add the next word into the
    # string followed by a space
    for value in words:
        if len(temp_str + value) + 1 <= 50:
            temp_str += value + " "
            if value == words[-1]:
                print(f"█ {temp_str:<50} █")
        else:
        # if it's greater than 50 print the line and set the tep string to the current word.
            print(f"█ {temp_str:<50} █")
            temp_str = value + " "
    print(f"█  {' ':^48}  █")
    print("█" * line_len)

def opt_format(options: tuple):
    formatted_dict = tup2dict(options)
    print(f"█  {' ':^48}  █")
    for key, selection in formatted_dict.items():
        print(f"█ {key+') '+selection[0]: <50} █")
        # print(f"{selection[1]}")
    print(f"█  {' ':^48}  █")
    print("█" * line_len)
    return formatted_dict

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tup2dict(option_tup: tuple):
    opt_dictionary = {}
    letters = [chr(x) for x in range(ord('a'), ord('z') + 1)] 
    opt_zip = list(zip(letters, option_tup))
    for letter, loc_data in opt_zip:
        # print(f"{letter}) {loc_data}")
        opt_dictionary.update({letter: loc_data})
    return opt_dictionary
