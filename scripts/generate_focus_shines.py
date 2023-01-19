from hoi_parser import parse_file, save_as_file

focus_path = "C:/Users/nectot/Documents/Paradox Interactive/Hearts of Iron IV/mod/pvp/interface/vallhale_focuses.gfx"
shine_dir = "C:/Users/nectot/Documents/Paradox Interactive/Hearts of Iron IV/mod/pvp/interface"

focuses = parse_file(focus_path, 'vallhale_focuses.gfx')

shines = {'spriteTypes': {}}
for index, focus in enumerate(focuses['spriteTypes'].keys()):
    contents = focuses['spriteTypes'][focus]
    print(contents)
    shines['spriteTypes']['spriteType!' + str(index)] = {
        'name': contents['name'] + '_shine',
		'texturefile': contents['texturefile'],
		'effectFile': 'gfx/FX/buttonstate.lua',
		'animation': {
			'animationmaskfile': contents['texturefile'],
			'animationtexturefile': 'gfx/interface/goals/shine_overlay.dds',    # <- the animated file
			'animationrotation': -90.0,        # -90 clockwise 90 counterclockwise(by default)
			'animationlooping': 'no',            # yes or no ;)
			'animationtime': 0.75,                # in seconds
			'animationdelay': 0,         # in seconds
			'animationblendmode': '"add"',       #add, multiply, overlay
			'animationtype': '"scrolling"',      #scrolling, rotating, pulsing
			'animationrotationoffset': { 'x': 0.0, 'y': 0.0 },
			'animationtexturescale': { 'x': 1.0, 'y': 1.0 }
		},
		'animation!2': {
			'animationmaskfile': contents['texturefile'],
			'animationtexturefile': 'gfx/interface/goals/shine_overlay.dds',    # <- the animated file
			'animationrotation': 90.0,        # -90 clockwise 90 counterclockwise(by default)
			'animationlooping': 'no',            # yes or no ;)
			'animationtime': 0.75,                # in seconds
			'animationdelay': 0,         # in seconds
			'animationblendmode': '"add"',       #add, multiply, overlay
			'animationtype': '"scrolling"',      #scrolling, rotating, pulsing
			'animationrotationoffset': { 'x': 0.0, 'y': 0.0 },
			'animationtexturescale': { 'x': 1.0, 'y': 1.0 }
		},
		'legacy_lazy_load': 'no'
    }

shines['_name'] = 'vallhale_focuses_shine.gfx'
save_as_file(shines, shine_dir)