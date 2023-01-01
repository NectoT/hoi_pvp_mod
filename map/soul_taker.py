from pathlib import Path

new_directory_path = "C:/Users/nectot/Documents/Paradox Interactive/Hearts of Iron IV/mod/pvp/history/countries"
directory = Path(new_directory_path)

for filepath in directory.iterdir():
    name = filepath.name
    with open(new_directory_path + "/" + name, 'w') as file:
        pass
        #file.write("capital = 1")

print("made empty files")