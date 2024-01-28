import functions as fnc
import map as m

cur_position = m.map["title_screen"]
while True:
    # this will update the position of the player and show the prompt for that area.
    # This function grabs the location name, location text, and the location options
    new_loc = fnc.prompt(cur_position["loc_name"], cur_position["loc_text"], cur_position["loc_opt"])
    cur_position = m.map[new_loc]
