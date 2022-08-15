from itertools import combinations, product

XTRACK_VS_FREQ = {'0XX0': 12,
                '0X0X': 8,
                'X0X0': 8,
                'X00X': 7,
                '000X': 3,
                'X000': 3,
                '0X00': 1,
                '00X0': 1}

COLORS = [1, 2, 3, 4]

def x2color(x_track, color):
    color_track = x_track.replace('X', str(color))
    return color_track


def zip_ctracks(ctrack1, ctrack2):
    ctrack_zipped = ''
    for i, _ in enumerate(ctrack1):
        char1 = ctrack1[i]
        char2 = ctrack2[i]
        if char1 == '0':
            ctrack_zipped += char2
        elif char2 == '0':
            ctrack_zipped += char1
        else:
            return None
    return ctrack_zipped


def build_ctrack_vs_freq(color, xtrack_vs_freq):
    ctrack_vs_freq = {}
    for x_track, freq in xtrack_vs_freq.items():
        color_track = x2color(x_track, color)
        ctrack_vs_freq[color_track] = freq
    return ctrack_vs_freq


def pair_dict_keys(dict1, dict2):
    keys1 = dict1.keys()
    keys2 = dict2.keys()
    
    all_key_pairs = [(k1, k2) for k2 in keys2
                         for k1 in keys1]
    return all_key_pairs


def is_exhausted(color_dict, ctrack):
    freq = color_dict[ctrack]
    if freq == 0:
        print(f"Track {ctrack1} reached its limit.")
        return True
    return False

ctrack_vs_freq_list = [build_ctrack_vs_freq(color, XTRACK_VS_FREQ) 
                       for color in COLORS]
    
deck = []
zipped_list1 = []
for dict1, dict2 in combinations(ctrack_vs_freq_list, 2):
    ctrack_all_pairs = pair_dict_keys(dict1, dict2)
    
    for ctrack1, ctrack2 in ctrack_all_pairs:
        if is_exhausted(dict1, ctrack1) or is_exhausted(dict2, ctrack2):
            break
        
        ctrack_zipped = zip_ctracks(ctrack1, ctrack2)
        if not ctrack_zipped is None:
            dict1[ctrack1] -= 1
            dict2[ctrack2] -= 1
            
            if '0' in ctrack_zipped:
                zipped_list1.append(ctrack_zipped)
            else:
                deck.append(ctrack_zipped)
  
zipped_list2 = []
for ctrack_z in zipped_list1:
    for i, a_dict in enumerate(ctrack_vs_freq_list):
        color = str(i + 1)
        if not color in ctrack_z:
            for ctrack_o in a_dict.keys():
                ctrack_zipped = zip_ctracks(ctrack_z, ctrack_o)
                if ctrack_zipped is None:
                    zipped_list2.append(ctrack_z)
                    pass
                    #print(f"Tracks {ctrack1} and {ctrack2} can't be zipped.")
                else:
                    while a_dict[ctrack_o] != 0: 
                        #print(ctrack_zipped)
                        a_dict[ctrack_o] -= 1
                        
                        if '0' in ctrack_zipped:
                            zipped_list2.append(ctrack_zipped)
                        else:
                            deck.append(ctrack_zipped)