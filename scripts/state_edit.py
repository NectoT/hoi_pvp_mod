from hoi_parser import save_as_file, parse_file
from os import listdir

def set_buildings(state, buildings):
    state['state']['history']['buildings'] = buildings

state_path = "C:/Users/nectot/Documents/Paradox Interactive/Hearts of Iron IV/mod/pvp/history/states"

victory_points = {
    521: 50, 520: 50, 700: 20, 699: 20, 568: 15, 565: 15, 618: 15, 617: 15, 773: 10, 772: 10,
    839: 15, 848: 15, 629: 20, 630: 20, 649: 5, 652: 5, 610: 1, 592: 1, 591: 1, 590: 1, 508: 1,
    509: 1, 841: 10, 846: 10, 842: 1, 845: 1, 445: 5, 446: 5, 696: 10, 703: 10, 830: 3, 825: 3,
    720: 3, 712: 3, 632: 1, 633: 1, 897: 1, 898: 1, 930: 20, 931: 20, 963: 50, 964: 50, 1042: 15,
    1045: 15, 1001: 5, 1002: 5, 1035: 3, 1034: 3, 1016: 1, 998: 1, 1015: 1, 997: 1, 1097: 1, 
    1058: 1, 1098: 1, 1059: 1
}

countries = {
    'EVA': [
        31, 37, 39, 67, 71, 33, 69, 35, 48, 75, 73, 77, 87, 89, 57, 59, 99, 55, 79, 91, 93, 
        51, 53, 63, 65, 61, 49, 97, 82, 81, 84, 27, 28, 29, 3, 5, 85, 95, 43, 44, 45
    ],
    'WVA': [
        64, 52, 94, 96, 101, 83, 60, 62, 50, 92, 100, 98, 90, 78, 80, 86, 54, 42, 68, 88, 78,
        74, 72, 32, 36, 66, 70, 30, 38, 34, 47, 56, 68, 24, 25, 26, 2, 4, 76, 40, 41, 46, 58, 1
    ],
    'FEI': [14, 16, 18, 20, 22, 8, 9, 10, 6],
    'EGL': [15, 17, 19, 21, 23, 11, 12, 13, 7]
}

cores = {
    'TOA': [24, 25, 26],
    'TAM': [27, 28, 29]
}

impassable_states = [40, 41, 46, 43, 44, 45, 1]

states = []
for filename in listdir(state_path):
    state = parse_file(state_path + "/" + filename, filename)
    if 'state' not in state or 'provinces' not in state['state']:
        continue
    
    state['state']['history'] = {}
    for country in countries:
        if int(state['state']['id']) in countries[country]:
            state['state']['history']['owner'] = country
    vp_amount = 0
    for province in state['state']['provinces']:
        if int(province) in victory_points:
            vp_amount += 1
            vp_string = 'victory_points!' + str(vp_amount)
            state['state']['history'][vp_string] = {}
            state['state']['history'][vp_string][province] = None
            state['state']['history'][vp_string][victory_points[int(province)]] = None
    
    if int(state['state']['id']) in impassable_states:
        state['state']['impassable'] = 'yes'
    
    for tag in cores:
        if int(state['state']['id']) in cores[tag]:
            state['state']['history']['add_core_of'] = tag

    states.append(state)

states = [None] + sorted(states, key=lambda s: int(s['state']['id']))

for id in [82, 101]:
    states[id]['state']['resources'] = {'oil': 80}
for id in [6, 7]:
    states[id]['state']['resources'] = {'oil': 110}
for id in [62, 63]:
    states[id]['state']['resources'] = {'chromium': 20, 'steel': 8}
for id in [24, 27]:
    states[id]['state']['resources'] = {'rubber': 180}
for id in [26, 29]:
    states[id]['state']['resources'] = {'rubber': 60}
for id in [98, 99]:
    states[id]['state']['resources'] = {'tungsten': 140}
for id in [98, 99]:
    states[id]['state']['resources'] = {'tungsten': 140}
for id in [90, 91]:
    states[id]['state']['resources'] = {'tungsten': 36, 'steel': 80}
for id in [74, 75]:
    states[id]['state']['resources'] = {'steel': 20}
for id in [56, 57]:
    states[id]['state']['resources'] = {'chromium': 50}
for id in [88, 89]:
    states[id]['state']['resources'] = {'aluminium': 100}
for id in [8, 13]:
    states[id]['state']['resources'] = {'steel': 170, 'aluminium': 24}
for id in [15, 14]:
    states[id]['state']['resources'] = {'chromium': 60}

capital_buildings = {
    'infrastructure': 4,
    'arms_factory': 1,
    'industrial_complex': 5
}

big_city_buildings = {
    'infrastructure': 3,
    'arms_factory': 1,
    'industrial_complex': 3
}

undeveloped_area_buildings = {
    'infrastructure': 1
}

for id in [82, 101, 52, 53, 60, 61, 62, 63, 27, 24, 10, 12]:
    set_buildings(states[id], undeveloped_area_buildings)

set_buildings(states[32], capital_buildings)
set_buildings(states[33], capital_buildings)

set_buildings(states[34], {
    'infrastructure': 3,
    'arms_factory': 2,
    'industrial_complex': 2,
    'dockyard': 1,
    839: {
        'naval_base': 5
    }
})

set_buildings(states[35], {
    'infrastructure': 3,
    'arms_factory': 2,
    'industrial_complex': 2,
    'dockyard': 1,
    848: {
        'naval_base': 5
    }
})

set_buildings(states[69], {
    'infrastructure': 3,
    'dockyard': 3,
    503: {
        'naval_base': 5
    }
})

set_buildings(states[68], {
    'infrastructure': 3,
    'dockyard': 3,
    501: {
        'naval_base': 5
    }
})

set_buildings(states[85], {
    'infrastructure': 1,
    434: {
        'naval_base': 3
    }
})
set_buildings(states[86], {
    'infrastructure': 1,
    437: {
        'naval_base': 3
    }
})

set_buildings(states[83], {
    'infrastructure': 1,
    431: {
        'naval_base': 3
    }
})
set_buildings(states[84], {
    'infrastructure': 1,
    432: {
        'naval_base': 3
    }
})

set_buildings(states[80], {
    'infrastructure': 1,
    'industrial_complex': 1,
    'dockyard': 1,
    445: {
        'naval_base': 5
    }
})
set_buildings(states[80], {
    'infrastructure': 1,
    'industrial_complex': 1,
    'dockyard': 1,
    446: {
        'naval_base': 5
    }
})

for id in [78, 79]:
    set_buildings(states[id], {
        'infrastructure': 1,
        'arms_factory': 1,
        'air_base': 1
    })

set_buildings(states[58], {
    'infrastructure': 2,
    'industrial_complex': 4,
    'dockyard': 1
})
set_buildings(states[59], {
    'infrastructure': 2,
    'industrial_complex': 4,
    'dockyard': 1
})

set_buildings(states[30], {
    'infrastructure': 2,
    'industrial_complex': 3,
    'arms_factory': 1
})
set_buildings(states[31], {
    'infrastructure': 2,
    'industrial_complex': 3,
    'arms_factory': 1
})

for id in [70, 71, 66, 67]:
    set_buildings(states[id], {
        'infrastructure': 3,
        'industrial_complex': 1,
    })

for id in [36, 37]:
    set_buildings(states[id], {
        'infrastructure': 3,
        'industrial_complex': 2,
        'arms_factory': 2
    })

for id in [42, 87]:
    set_buildings(states[id], {
        'infrastructure': 3,
        'arms_factory': 3
    })

for id in [72, 73, 74, 75, 76, 77, 37, 38]:
    set_buildings(states[id], {
        'infrastructure': 3,
    })

for id in [54, 55]:
    set_buildings(states[id], {
        'infrastructure': 3,
        'industrial_complex': 3
    })

for id in [94, 95]:
    set_buildings(states[id], {
        'infrastructure': 2,
        'arms_factory': 2,
        'air_base': 4
    })

for id in [52, 53]:
    set_buildings(states[id], {
        'infrastructure': 2,
        'industrial_complex': 1,
        'air_base': 3
    })

for id in [50, 51]:
    set_buildings(states[id], {
        'infrastructure': 2,
        'industrial_complex': 3,
    })

for id in [92, 93, 96, 97, 64, 65, 38, 39]:
    set_buildings(states[id], {
        'infrastructure': 2,
    })

for id in [88, 89]:
    set_buildings(states[id], {
        'infrastructure': 2,
        'industrial_complex': 1,
        'air_base': 3
    })

for id in [90, 91, 98, 99]:
    set_buildings(states[id], {
        'infrastructure': 2,
        'industrial_complex': 1,
    })

set_buildings(states[56], {
    'infrastructure': 2,
    'industrial_complex': 1,
    863: {
        'naval_base': 4
    }
})
set_buildings(states[56], {
    'infrastructure': 2,
    'industrial_complex': 1,
    864: {
        'naval_base': 4
    }
})

set_buildings(states[26], {
    'infrastructure': 1,
    'industrial_complex': 1,
    235: {
        'naval_base': 2
    }
})
set_buildings(states[29], {
    'infrastructure': 1,
    'industrial_complex': 1,
    214: {
        'naval_base': 2
    }
})

set_buildings(states[25], {
   'infrastructure': 1,
    'industrial_complex': 1,
    279: {
        'naval_base': 3
    } 
})
set_buildings(states[28], {
   'infrastructure': 1,
    'industrial_complex': 1,
    280: {
        'naval_base': 3
    } 
})

set_buildings(states[4], {
   'infrastructure': 1,
    1136: {
        'naval_base': 3
    } 
})
set_buildings(states[5], {
   'infrastructure': 1,
    1137: {
        'naval_base': 3
    } 
})

set_buildings(states[6], {
    'infrastructure': 1,
    'industrial_complex': 1,
    1232: {
        'naval_base': 3
    }
})
set_buildings(states[7], {
    'infrastructure': 1,
    'industrial_complex': 1,
    1233: {
        'naval_base': 3
    }
})

set_buildings(states[18], {
    'infrastructure': 3,
    'industrial_complex': 4,
    'dockyard': 1,
    936: {
        'naval_base': 4
    }
})
set_buildings(states[19], {
    'infrastructure': 3,
    'industrial_complex': 4,
    'dockyard': 1,
    937: {
        'naval_base': 4
    }
})

set_buildings(states[20], {
    'infrastructure': 4,
    'industrial_complex': 1,
    'arms_factory': 3,
    'dockyard': 3,
    953: {
        'naval_base': 5
    }
})
set_buildings(states[21], {
    'infrastructure': 4,
    'industrial_complex': 1,
    'arms_factory': 3,
    'dockyard': 3,
    954: {
        'naval_base': 5
    }
})

set_buildings(states[22], {
    'infrastructure': 2,
    'arms_factory': 1,
    'dockyard': 2,
    'air_base': 3,
    1003: {
        'naval_base': 5
    }
})
set_buildings(states[23], {
    'infrastructure': 2,
    'arms_factory': 1,
    'dockyard': 2,
    'air_base': 3,
    1008: {
        'naval_base': 5
    }
})

set_buildings(states[14], {
    'infrastructure': 2,
    'arms_factory': 2,
    1034: {
        'naval_base': 4
    }
})
set_buildings(states[15], {
    'infrastructure': 2,
    'arms_factory': 2,
    1035: {
        'naval_base': 4
    }
})

for id in [16, 17]:
    set_buildings(states[id], {
        'infrastructure': 2,
        'industrial_complex': 2,
    })

set_buildings(states[9], {
    'infrastructure': 2,
    'industrial_complex': 1,
    'dockyard': 1,
    1042: {
        'naval_base': 4
    }
})
set_buildings(states[11], {
    'infrastructure': 2,
    'industrial_complex': 1,
    'dockyard': 1,
    1045: {
        'naval_base': 4
    }
})

set_buildings(states[8], {
    'infrastructure': 1,
    'arms_factory': 1,
    1097: {
        'naval_base': 4
    }
})
set_buildings(states[13], {
    'infrastructure': 1,
    'arms_factory': 1,
    1098: {
        'naval_base': 4
    }
})

for state in states[1:]:
    save_as_file(state, state_path)

print("Finished")