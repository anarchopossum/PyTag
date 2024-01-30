import yaml
from pathlib import Path

def test_yamlindex():
    story_list = []
    story_file: None
    p = Path("stories")

    # for each yaml file in directory
    # Open the file
    # safe_load it using yaml
    # assert that it's a string
    for each in list(p.glob('*.[yaml][yml]')):
        with open(each) as file:
            story_file = yaml.safe_load(file)
            
            # assert type(yamlindex(story_file['game_name'])) == str

