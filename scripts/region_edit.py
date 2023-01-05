from os import listdir
from hoi_parser import save_as_file, parse_file

original_region_path = "C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/map/strategicregions"
region_path = "C:/Users/nectot/Documents/Paradox Interactive/Hearts of Iron IV/mod/pvp/map/strategicregions"


coastal_mild_climate_ids = [5, 6, 72, 73, 1, 2]
coastal_mild_climate = {
    'period!1': {
        'between': { 0.0: None, 0.2: None },
        'temperature': { -10.0: None, 7: None },
        'no_phenomenon': 0.5,
        'rain_light': 0,
        'rain_heavy': 0,
        'snow': 0.250,
        'blizzard': 0.1,
        'arctic_water': 0.000,
        'mud': 0.100,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
    'period!2': {
        'between': { 1.2: None, 0.4: None },
        'temperature': { -1.0: None, 16: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.25,
        'rain_heavy': 0,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0.100,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
    'period!3': {
        'between': { 1.4: None, 0.11: None },
        'temperature': { 5: None, 27: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.6,
        'rain_heavy': 0.1,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0.200,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
    'period!4': {
        'between': { 1.11: None, 30.11: None },
        'temperature': { -14: None, 1: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.25,
        'rain_heavy': 0.1,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0.100,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
}

central_climate_ids = [10, 11, 19, 20]
central_climate = {
    'period!1': {
        'between': { 0.11: None, 29.0: None },
        'temperature': { -21: None, -3: None },
        'no_phenomenon': 0.5,
        'rain_light': 0,
        'rain_heavy': 0,
        'snow': 0.4,
        'blizzard': 0.1,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0.100
	},
    'period!2': {
        'between': { 0.1: None, 0.2: None },
        'temperature': { -30: None, -10: None },
        'no_phenomenon': 0.5,
        'rain_light': 0,
        'rain_heavy': 0,
        'snow': 0.1,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
    'period!3': {
        'between': { 1.2: None, 30.2: None },
        'temperature': { -5: None, 12: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.1,
        'rain_heavy': 0,
        'snow': 0.1,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
    'period!4': {
        'between': { 0.3: None, 29.3: None },
        'temperature': { 4: None, 18: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.4,
        'rain_heavy': 0,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0.4,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
    'period!5': {
        'between': { 0.4: None, 30.7: None },
        'temperature': { 12: None, 28: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.2,
        'rain_heavy': 0,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
    'period!6': {
        'between': { 0.4: None, 30.7: None },
        'temperature': { 12: None, 28: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.2,
        'rain_heavy': 0,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
    'period!7': {
        'between': { 0.8: None, 30.9: None },
        'temperature': { 5: None, 23: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.5,
        'rain_heavy': 0.2,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0.2,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
    'period!8': {
        'between': { 0.10: None, 29.10: None },
        'temperature': { -3: None, 16: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.3,
        'rain_heavy': 0.2,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0.1,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
}

mountain_climate_ids = [70, 71]
mountain_climate = {
    'period': {
        'between': { 0.0: None, 30.11: None },
        'temperature': { -10: None, 0: None },
        'no_phenomenon': 0.5,
        'rain_light': 0,
        'rain_heavy': 0,
        'snow': 0,
        'blizzard': 0.4,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0.100
	},
}

meditterenian_climate_ids = [69]
meditterenian_climate = {
    'period!1': {
        'between': { 0.11: None, 30.2: None },
        'temperature': { 14: None, 25: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.1,
        'rain_heavy': 0.2,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
    'period!2': {
        'between': { 0.3: None, 29.5: None },
        'temperature': { 18: None, 30: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.15,
        'rain_heavy': 0,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
    'period!3': {
        'between': { 0.6: None, 30.9: None },
        'temperature': { 20: None, 38: None },
        'no_phenomenon': 0.5,
        'rain_light': 0,
        'rain_heavy': 0,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
    'period!4': {
        'between': { 0.10: None, 30.11: None },
        'temperature': { 20: None, 38: None },
        'no_phenomenon': 0.3,
        'rain_light': 0.2,
        'rain_heavy': 0.6,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
}

desert_climate_ids = [9]
desert_climate = {
    'period': {
        'between': { 0.0: None, 30.11: None },
        'temperature': { 28: None, 42: None },
        'no_phenomenon': 0.5,
        'rain_light': 0,
        'rain_heavy': 0,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.4,
        'min_snow_level': 0.000
	},
}

cold_sea_climate_ids = [56, 54, 57, 55, 37, 39, 43, 40, 38, 44, 45]
cold_sea_climate = {
    'period': {
        'between': { 0.0: None, 30.11: None },
        'temperature': { -20: None, -4: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.1,
        'rain_heavy': 0.45,
        'snow': 0.2,
        'blizzard': 0.3,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
}

normal_sea_climate_ids = []
normal_sea_climate = {
    'period': {
        'between': { 0.0: None, 30.11: None },
        'temperature': { 5: None, 15: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.1,
        'rain_heavy': 0.30,
        'snow': 0.1,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0.000
	},
}

mild_central_climate_ids = [3, 4, 7, 8]
mild_central_climate = {
    'period!1': {
        'between': { 0.11: None, 0.2: None },
        'temperature': { -15: None, 2: None },
        'no_phenomenon': 0.5,
        'rain_light': 0,
        'rain_heavy': 0,
        'snow': 0.4,
        'blizzard': 0.1,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0
	},
    'period!2': {
        'between': { 1.2: None, 30.2: None },
        'temperature': { 0: None, 16: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.2,
        'rain_heavy': 0,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0.3,
        'sandstorm': 0.000,
        'min_snow_level': 0
	},
    'period!3': {
        'between': { 0.3: None, 30.4: None },
        'temperature': { 10: None, 24: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.2,
        'rain_heavy': 0.1,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0.1,
        'sandstorm': 0.000,
        'min_snow_level': 0
	},
    'period!4': {
        'between': { 0.5: None, 30.7: None },
        'temperature': { 16: None, 30: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.2,
        'rain_heavy': 0.2,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0
	},
    'period!5': {
        'between': { 0.8: None, 30.9: None },
        'temperature': { 10: None, 24: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.4,
        'rain_heavy': 0.1,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0.1,
        'sandstorm': 0.000,
        'min_snow_level': 0
	},
    'period!6': {
        'between': { 0.10: None, 29.10: None },
        'temperature': { 2: None, 17: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.3,
        'rain_heavy': 0.1,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0.1,
        'sandstorm': 0.000,
        'min_snow_level': 0
	},
}

harsh_coastal_climate_ids = [41, 42]
harsh_coastal_climate = {
    'period': {
        'between': { 0.9: None, 29.3: None },
        'temperature': { -17: None, 5: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.3,
        'rain_heavy': 0,
        'snow': 0.6,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0
	},
    'period': {
        'between': { 0.4: None, 29.8: None },
        'temperature': { 0: None, 16: None },
        'no_phenomenon': 0.5,
        'rain_light': 0.6,
        'rain_heavy': 0,
        'snow': 0,
        'blizzard': 0,
        'arctic_water': 0.000,
        'mud': 0,
        'sandstorm': 0.000,
        'min_snow_level': 0
	},
}

for filename in listdir(region_path):
    region = parse_file(region_path + "/" + filename, filename)
    if 'strategic_region' not in region:
        continue

    if int(region['strategic_region']['id']) in harsh_coastal_climate_ids:
        region['strategic_region']['weather'] = harsh_coastal_climate
    elif int(region['strategic_region']['id']) in mild_central_climate_ids:
        region['strategic_region']['weather'] = mild_central_climate
    elif int(region['strategic_region']['id']) in central_climate_ids:
        region['strategic_region']['weather'] = central_climate
    elif int(region['strategic_region']['id']) in cold_sea_climate_ids:
        region['strategic_region']['weather'] = cold_sea_climate
    elif int(region['strategic_region']['id']) in meditterenian_climate_ids:
        region['strategic_region']['weather'] = meditterenian_climate
    elif int(region['strategic_region']['id']) in desert_climate_ids:
        region['strategic_region']['weather'] = desert_climate
    elif int(region['strategic_region']['id']) in coastal_mild_climate_ids:
        region['strategic_region']['weather'] = coastal_mild_climate
    elif int(region['strategic_region']['id']) in mountain_climate_ids:
        region['strategic_region']['weather'] = mountain_climate
    else:
        region['strategic_region']['weather'] = normal_sea_climate
    save_as_file(region, region_path)

    # if int(region['strategic_region']['id']) == 4:
    #     print(mild_central_climate)
    #     print(region['strategic_region']['weather'])
    #     break

print("Finished")