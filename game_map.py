import yaml
import functions as fnc
from pathlib import Path
from functools import partial


class SwitchGame:
    def __init__(self, new_game: str):
        self.new_game = new_game

class Gamelist:

    def __init__(self):
        self.gme_list = []
        self.selected_map = None

    def generate_list(self):
        p = Path("stories/")
        # for each yaml file in directory
        # Open the file
        # safe_load it using yaml (converts it to Dictionary)
        # add game_object to list
        # try to find a way to add yml and yaml
        # print("glob", list(p.glob('*.{yaml,yml}')))
        for yaml_file in list(p.glob('*.yaml')):
            with open(yaml_file) as file:
                safeloaded_story = yaml.safe_load(file)
                processed_story = Game(safeloaded_story)
                self.gme_list.append(processed_story)

    def name_list(self):
        game_selections = []
        for game_obj in self.gme_list:
            # Todo: Find a way to get the game object to give information to
            # the map confirmation screen
            temp_tup = (game_obj.name, SwitchGame(game_obj.name))
            print(temp_tup)


            game_selections.append(temp_tup)
        game_selections.append(("Back","title_screen"))
        return game_selections

    def get_map(self, game_name):
        for game in self.gme_list:
            if game.name == game_name:
                return game.map
        raise KeyError(f"Cannot find game {game_name}")

class Game:
    def __init__(self,gme_dict) -> None:
        self.name = gme_dict["game_name"]
        # .get to state optionality
        self.description = gme_dict.get("description", None)
        self.map = gme_dict["map"]

def game_select(menu_map, game_obj):
   menu_map["game_confirmation"]["loc_name"] = game_obj.name
   menu_map["game_confirmation"]["loc_title"] = game_obj.description
   menu_map["game_confirmation"]["loc_opt"] = [("Accept",game_start(game_obj.map)), ("Back","game_selection")]

def game_start(game_map):
       cur_position = game_map["title_screen"]
       while True:
           new_loc = fnc.prompt(cur_position["loc_name"],cur_position["loc_text"],cur_position["loc_opt"])
           cur_position = game_map[new_loc]
           

def make_main_menu(map_opt):
    return {
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
                "loc_name" : "",
                "loc_text" : "",
                "loc_opt" : ["map_switch(None)",("Back", "game_selection"),]
                },
        }
