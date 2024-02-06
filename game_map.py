import yaml
from pathlib import Path

class Gamelist:

    def __init__(self):
        self.gme_list = []

    def generate_list(self):
        p = Path("stories/")
        # for each yaml file in directory
        # Open the file
        # safe_load it using yaml (converts it to Dictionary)
        # add game_object to list

        # try to find a way to add yml and yaml
        # print("glob", list(p.glob('*.{yaml,yml}')))
        for each in list(p.glob('*.yaml')):
            with open(each) as file:
                safeloaded_story = yaml.safe_load(file)
                processed_story = Game(safeloaded_story)
                print(processed_story)
                # story_object = Game(processed_story)
                self.gme_list.append(processed_story)

                print(self.gme_list)
        # return self.gme_list

    def name_list(self):
        game_selections = []
        for each in self.gme_list:
            temp_tup = (each.name, each)
            game_selections.append(temp_tup)
        game_selections.append(("Back","title_screen"))
        return game_selections 



class Game:
    def __init__(self,gme_dict) -> None:
        self.name = gme_dict["game_name"]
        # .get to state optionality
        self.description = gme_dict.get("description", None)
        self.map = gme_dict["map"]

def map_switch():
    pass




test_list = Gamelist()
test_list.generate_list()
map_opt = test_list.name_list()

menu_map = {
        "title_screen": {
            "loc_name" : "Welcome to PyTAG",
            "loc_text" : """
            Welcome to the test game. You can quit the game at any point just type q and hit enter. Best of luck! This is currently a demo. If you would like to make your own story. try to modify the map.py file
            type the letter a to go to the next area
            """,
            "loc_opt": [("Start Game", "game_selection"),
                        ("Options", "options")]
            },

        "game_selection": {
            "loc_name" : "Game Select",
            "loc_text" : """
            Select a Game to play
            """,
            # Grabs the list of maps
            "loc_opt": map_opt 
        },
        "game_confirmation": {
            # Grabs the selected map's Name, description, and data
            "loc_name" : None,
            "loc_text" : None,
            "loc_opt" : [(None, None),("Back", "game_selection"),]
            },

    }

map = menu_map
