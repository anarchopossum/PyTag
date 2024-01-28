map = {
        "title_screen": {
            "loc_name" : "Game Title",
            "loc_text" : """
            Welcome to the test game. You can quit the game at any point just type q and hit enter. Best of luck! This is currently a demo. If you would like to make your own story. try to modify the map.py file
            type the letter a to go to the next area
            """,
            "loc_opt": (("Next", "introduction"),)
            },

        "introduction": {
            "loc_name" : "Intro",
            "loc_text" : """
            Welcome to Pytag (Python Text Adventure Game)! With this engine you can make your own text adventure games. Pytag was created with expandability in mind, So if you are just getting into coding, or an expert you can comfortably
            start building your own world and stories.
            """,
            "loc_opt": (("Start Screen", "title_screen"),("Next","introduction2"),)
        }
    }
