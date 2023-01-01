from PIL import Image
import pandas

colors = {}

definition_path = "C:/Users/nectot/Documents/Paradox Interactive/Hearts of Iron IV/mod/pvp/map/definition.csv"
path = "C:/Users/nectot/Documents/Paradox Interactive/Hearts of Iron IV/mod/pvp/map/provinces.bmp"
pixels = Image.open(path).getdata()

for pixel in pixels:
    colors[pixel[0] * 10**6 + pixel[1] * 10**3 + pixel[2]] = True

definition: pandas.DataFrame = pandas.read_csv(
    definition_path,
    names=['id', 'r', 'g', 'b', 'land_type', 'is_coast', 'terrain', 'continent'],
    index_col=None,
    sep=";"
)

province_counter = 0

for i, color in enumerate(colors):
    colors = [
        int(color / 10**6),
        int(color / 10**3 % 1000),
        color % 1000
    ]


    mask = (definition['r'] == colors[0]) & (definition['g'] == colors[1]) & (definition['b'] == colors[2])
    if not mask.any():
        province_counter += 1
        last_id = definition.loc[len(definition) - 1, 'id']
        definition.loc[len(definition)] = [last_id + 1, *colors, 'sea', 'false', 'ocean', 7]

definition.to_csv(definition_path, header=False, index=False, sep=";")

print("{0} provinces added".format(province_counter))
