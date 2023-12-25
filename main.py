import functions as fnc
import map as m

# loc_name = "Testing Grounds"
# loc_text = """
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean velit felis, aliquam ultricies nulla et, luctus tempus lorem. Proin tincidunt odio sed quam rutrum interdum. Nulla vitae libero quis libero blandit accumsan eget a sem. Praesent nec ultrices sem, ut ultricies felis. Donec sollicitudin mi auctor libero tempus tincidunt. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin viverra nisl in tellus condimentum consectetur. Fusce blandit maximus nisl a finibus. Vivamus vehicula, purus nec condimentum placerat, dui odio sodales libero, sed posuere odio metus in est. Donec nec aliquam diam. Fusce in aliquet felis. Donec posuere odio quis nunc cursus, a suscipit elit placerat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nullam in lorem tortor. Cras scelerisque non urna in faucibus. Nullam lobortis, felis ac placerat convallis, risus libero ultrices lorem, ac pretium diam ante non orci.
# """
# loc_opt = {
#         "a": "Town",
#         "b": "Park",
#         "c": "Library"
#         }
cur_position = m.map["title screen"]
while True:
    new_loc = fnc.prompt(cur_position["loc_name"], cur_position["loc_text"], cur_position["loc_opt"])
    cur_position = m.map[new_loc]
