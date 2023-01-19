import re

def parse_file(path, name)->dict:
    regex = re.compile("\S+")
    r_comments = re.compile("#.*")

    keywords = {}

    with open(path, "r") as file:
        raw_text = file.read()
    filtered_text = raw_text.replace('"', "")
    filtered_text = filtered_text.replace("=", " = ")
    filtered_text = filtered_text.replace("{", " { ")
    filtered_text = filtered_text.replace("}", " } ")

    filtered_text = r_comments.sub("", filtered_text)
    regex_words = regex.findall(filtered_text)

    contents = {'_name': name, '_keywords': {}}
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
            new_dict['_keywords'] = {}
            stack[len(stack) - 1][current_keyword] = new_dict
            stack.append(new_dict)
            has_assignment = False
        elif word == "}":
            stack[-1].pop('_keywords')
            stack.pop()
        elif not has_assignment:
            current_keyword = word
            if current_keyword not in stack[-1]['_keywords']:
                stack[-1]['_keywords'][current_keyword] = 1
            else:
                stack[-1]['_keywords'][current_keyword] += 1
                current_keyword = current_keyword + '!' + str(stack[-1]['_keywords'][current_keyword])
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
            file.write(str(key).split("!")[0] + " ")
            newline = False
        elif type(contents[key]) is dict:
            file.write(str(key).split("!")[0] + " = { \n")
            _save_contents(contents[key], file, depth=(depth + 1), whitelist=whitelist, blacklist=blacklist)
            file.write("\t"*depth + "}\n")
            newline = True
        else:
            file.write(str(key).split("!")[0] + " = " + str(contents[key]).split("!")[0] + "\n")
            newline = True

def save_as_file(contents, directory_path):
    with open(directory_path + "/" + contents['_name'], "w") as file:
        _save_contents(contents, file)

def save_as_empty_file(contents, directory_path):
    with open(directory_path + "/" + contents['_name'], "w") as file:
        _save_contents(contents, file, whitelist=['state', 'id', 'manpower', 'state_category'])