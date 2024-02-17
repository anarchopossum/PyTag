import functions as fnc
import game_map as m

def main():
    # Creates Game List
    game_list = m.Gamelist()
    game_list.generate_list()
    map_opt = game_list.name_list()
    current_game = m.make_main_menu(map_opt)
    cur_position = current_game['title_screen']
    while True:
        # this will update the position of the player and show the prompt for that area.
        # This function grabs the location name, location text, and the location options
        new_loc = fnc.prompt(cur_position["loc_name"], cur_position["loc_text"], cur_position["loc_opt"])
        match new_loc:
            case str():
                cur_position = current_game[new_loc]
            case m.SwitchGame():
                print(new_loc.new_game)
                current_game = game_list.get_map(new_loc.new_game)
                print(current_game)
                cur_position = current_game['title_screen']

if __name__ == '__main__':
    main()
