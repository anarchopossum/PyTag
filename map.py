import yaml
from pathlib import Path

class gamelist:

    def __init__(self):
        self.gme_list = []
        p = Path("stories")
        # for each yaml file in directory
        # Open the file
        # safe_load it using yaml (converts it to Dictionary)
        # add Dictionary to list
        for each in list(p.glob('*.[yaml][yml]')):
            with open(each) as file:
                safeloaded_story = yaml.safe_load(file)
                processed_story = game(safeloaded_story)
                story_object = game(processed_story)
                self.gme_list.append(story_object)
        # return self.gme_list

    def namelist(self):
        for each in self.gme_list:
           pass 



class game:
    def __init__(self,gme_dict) -> None:
        self.name = gme_dict["game_name"]
        # .get to state optionality
        self.description = gme_dict.get("description", None)
        self.map = gme_dict["map"]

#def list_story(story_list):
#    for each in story_list:
#       pass 
#
#def story_collect():
#    story_list = []
#    p = Path("stories")
#    # for each yaml file in directory
#    # Open the file
#    # safe_load it using yaml (converts it to Dictionary)
#    # add Dictionary to list
#    for each in list(p.glob('*.[yaml][yml]')):
#        with open(each) as file:
#            processed_story = yaml.safe_load(file)
#            story_list.append(processed_story)
#    return story_list

map_opt = None

map = {
        "title_screen": {
            "loc_name" : "Welcome to PyTAG",
            "loc_text" : """
            Welcome to the test game. You can quit the game at any point just type q and hit enter. Best of luck! This is currently a demo. If you would like to make your own story. try to modify the map.py file
            type the letter a to go to the next area
            """,
            "loc_opt": (("Start Game", "game_selection"),
                        ("Options", "options"))
            },

        "game_selection": {
            "loc_name" : "Game Select",
            "loc_text" : """
            Select a Game to play
            """,
            "loc_opt": (("Main Menu", "title_screen"),("Next","introduction2"),)
        },
        "game_confirmation": None

    }

