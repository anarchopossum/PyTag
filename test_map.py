# from typing import assert_type
import yaml
import map as m
from pathlib import Path

#def test_yamlindex():
#    story_list = []
#    story_file: None
#    p = Path("stories")

    # for each yaml file in directory
    # Open the file
    # safe_load it using yaml
    # assert that it's a string
#    for each in list(p.glob('*.[yaml][yml]')):
#        with open(each) as file:
#            story_file = yaml.safe_load(file)
#            # assert type(yamlindex(story_file['game_name'])) == str

def test_yaml():
    filepath = Path("stories/test.yaml")
    with open(filepath) as file:
        file2dict = yaml.safe_load(file)
        assert type(file2dict) is dict
        assert file2dict["game_name"] == 'Tutorial'


def test_game():
    test_obj = None
    test_game = Path("stories/test.yaml")
    with open(test_game) as file:
        test_obj = m.Game(yaml.safe_load(file))
        assert type(test_obj) == m.Game
        assert test_obj.name == "Tutorial"
        assert type(test_obj.description) is str
        assert type(test_obj.map) is dict

def test_gamelist():
    test_list = m.Gamelist()
    test_list.generate_list()
    assert type(test_list) is m.Gamelist
    assert type(test_list.gme_list) is list
    assert len(test_list.gme_list) == 1
    for each in test_list.gme_list:
        assert type(each) is m.Game
        assert type(each.name) is str
        assert each.name == "Tutorial"

    # assert (test_list.gme_list[0]["game_name"]) == 'Tutorial'

