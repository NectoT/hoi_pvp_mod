from os import listdir
from hoi_parser import save_as_empty_file, parse_file

original_state_path = "C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states"
state_path = "C:/Users/nectot/Documents/Paradox Interactive/Hearts of Iron IV/mod/pvp/history/states"


min_id = 102
for filename in listdir(original_state_path):
    state = parse_file(original_state_path + "/" + filename, filename)
    if int(state['state']['id']) >= min_id:
        save_as_empty_file(state, state_path)

print("Finished")