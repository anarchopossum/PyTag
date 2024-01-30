import yaml
from pathlib import Path

class gamelist:
    def __init__(self) -> None:
        self.gme_list = []

class game:
    def __init__(self,gme_file) -> None:
        self.name = gme_file.get("game_name", None)
        self.description = gme_file.get("description", None)
        self.map = gme_file["map"]

def list_story(story_list):
    for each in story_list:
       pass 

def story_collect():
    story_list = []
    p = Path("stories")
    # for each yaml file in directory
    # Open the file
    # safe_load it using yaml
    # assert that it's a string
    for each in list(p.glob('*.[yaml][yml]')):
        with open(each) as file:
            processed_story = yaml.safe_load(file)
            story_list.append(processed_story)
    return story_list

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
            "loc_name" : "Intro",
            "loc_text" : """
            Welcome to Pytag (Python Text Adventure Game)! With this engine you can make your own text adventure games. Pytag was created with expandability in mind, So if you are just getting into coding, or an expert you can comfortably
            start building your own world and stories.
            """,
            "loc_opt": (("Main Menu", "title_screen"),("Next","introduction2"),)
        }
    }

