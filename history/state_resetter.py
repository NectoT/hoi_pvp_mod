from os import listdir
import re

def parse_file(path, name)->dict:
    regex = re.compile("\S+")
    r_comments = re.compile("#.*")

    with open(path, "r") as file:
        raw_text = file.read()
    filtered_text = raw_text.replace('"', "")
    filtered_text = filtered_text.replace("=", " = ")
    filtered_text = filtered_text.replace("{", " { ")
    filtered_text = filtered_text.replace("}", " } ")

    filtered_text = r_comments.sub("", filtered_text)
    regex_words = regex.findall(filtered_text)

    contents = {'_name': name}
    stack = [contents]
    current_keyword = None
    has_assignment = False
    for i in range(len(regex_words)):
        word = regex_words[i]
        if word == '=':
            has_assignment = True
            continue
        
        if word == "{":
            new_dict = {}
            stack[len(stack) - 1][current_keyword] = new_dict
            stack.append(new_dict)
            has_assignment = False
        elif word == "}":
            stack.pop()
        elif not has_assignment:
            current_keyword = word
            stack[len(stack) - 1][current_keyword] = None
        else:
            stack[len(stack) - 1][current_keyword] = word
            has_assignment = False
    return contents

def _save_contents(contents, file, depth=0, whitelist=None, blacklist=["_name"]):
    newline = True
    for key in contents:
        if whitelist is not None and key not in whitelist:
            continue
        if key in blacklist:
            continue
        
        if newline:
            file.write("\t"*depth)
        if contents[key] is None:
            file.write(key + " ")
            newline = False
        elif type(contents[key]) is dict:
            file.write(key + " = { \n")
            _save_contents(contents[key], file, depth=(depth + 1), whitelist=whitelist, blacklist=blacklist)
            file.write("\t"*depth + "}\n")
            newline = True
        else:
            file.write(key + " = " + contents[key] + "\n")
            newline = True

def save_state(state, directory_path):
    with open(directory_path + "/" + state['_name'], "w") as file:
        _save_contents(state, file)

def save_empty_state(state, directory_path):
    with open(directory_path + "/" + state['_name'], "w") as file:
        _save_contents(state, file, whitelist=['state', 'id', 'manpower', 'state_category'])

original_state_path = "C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states"
state_path = "C:/Users/nectot/Documents/Paradox Interactive/Hearts of Iron IV/mod/pvp/history/states"


min_id = 102
for filename in listdir(original_state_path):
    state = parse_file(original_state_path + "/" + filename, filename)
    if int(state['state']['id']) >= min_id:
        save_empty_state(state, state_path)

print("Finished")