# from typing import assert_type
import yaml
import game_map as m
from pathlib import Path

# tests if a yaml file can be converted to a dictionary
def test_yaml():
    filepath = Path("stories/test.yaml")
    with open(filepath) as file:
        file2dict = yaml.safe_load(file)
        assert type(file2dict) is dict
        assert file2dict["game_name"] == 'Tutorial'

# tests if a game object is generated from a dictionary
def test_game():
    test_obj = None
    test_game = Path("stories/test.yaml")
    with open(test_game) as file:
        test_obj = m.Game(yaml.safe_load(file))
        assert type(test_obj) == m.Game
        assert test_obj.name == "Tutorial"
        assert type(test_obj.description) is str
        assert type(test_obj.map) is dict

# tests to see if game_list object is generated with game objects inside
def test_gamelist():
    test_list = m.Gamelist()
    test_list.generate_list()
    assert type(test_list) is m.Gamelist
    assert type(test_list.gme_list) is list
    assert len(test_list.gme_list) == 2
    for each in test_list.gme_list:
        assert type(each) is m.Game
        assert type(each.name) is str
        # assert each.name == "Tutorial"

# returns a list of tuples with (game_name, game_object)
def test_name_list():
    test_list = m.Gamelist()
    test_list.generate_list()
    assert type(test_list.gme_list) is list
    assert len(test_list.gme_list) is 2
    final_list = test_list.name_list()
    print(f"final List: {final_list} ##")

    # When trying to find if something is a type of list rather than an empty one
    # use assert type
    assert type(final_list) is list
    assert type(final_list[0]) is tuple
    assert type(final_list[0][0]) is str
    assert type(final_list[0][1]) is m.Game

    


    # assert type(test_list.gme_list[0][1]) is m.Game
    # assert test_list.gme_list[0][0] is str


