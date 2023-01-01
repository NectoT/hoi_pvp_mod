from os import listdir
import re
import pandas

colors = {}

definition_path = "C:/Users/nectot/Documents/Paradox Interactive/Hearts of Iron IV/mod/pvp/map/definition.csv"

definition: pandas.DataFrame = pandas.read_csv(
    definition_path,
    names=['id', 'r', 'g', 'b', 'land_type', 'is_coast', 'terrain', 'continent'],
    index_col=None,
    sep=";"
)


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

state_path = "C:/Users/nectot/Documents/Paradox Interactive/Hearts of Iron IV/mod/pvp/history/states"

for filename in listdir(state_path):
    state: dict = parse_file(state_path + "/" + filename, filename)
    if 'state' not in state:
        continue
    for id in state['state']['provinces']:
        definition.at[int(id), 'terrain'] = "plains"
        definition.at[int(id), 'land_type'] = "land"
definition.to_csv(definition_path, header=False, index=False, sep=";")
print("Finished")