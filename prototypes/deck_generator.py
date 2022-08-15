from itertools import combinations, product

TRACK_VS_FREQ = {'0XX0': 12,
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


ctrack_vs_freq_list = []
for color in COLORS:
    ctrack_vs_freq = {}
    for x_track, freq in TRACK_VS_FREQ.items():
        color_track = x2color(x_track, color)
        ctrack_vs_freq[color_track] = freq
    ctrack_vs_freq_list.append(ctrack_vs_freq)
    
dicts_not_modified = [dict(a_dict) for a_dict in ctrack_vs_freq_list]
    
deck = []
zipped_list1 = []
for dict1, dict2 in combinations(ctrack_vs_freq_list, 2):
    ctrack_list1 = dict1.keys()
    ctrack_list2 = dict2.keys()
    
    ctrack_all_pairs = [(ctrack1, ctrack2) for ctrack2 in ctrack_list2
                         for ctrack1 in ctrack_list1]
    for ctrack1, ctrack2 in ctrack_all_pairs:
        freq1, freq2 = dict1[ctrack1], dict2[ctrack2]
        if freq1 == 0:
            print(f"Track {ctrack1} reached its limit.")
            break
        if freq2 == 0:
            print(f"Track {ctrack2} reached its limit.")
            break
        
        ctrack_zipped = zip_ctracks(ctrack1, ctrack2)
        if ctrack_zipped is None:
            pass
            #print(f"Tracks {ctrack1} and {ctrack2} can't be zipped.")
        else:
            while dict1[ctrack1] != 0 and  dict2[ctrack2] != 0: 
                #print(ctrack_zipped)
                dict1[ctrack1] -= 1
                dict2[ctrack2] -= 1
                
                if '0' in ctrack_zipped:
                    zipped_list1.append(ctrack_zipped)
                else:
                    deck.append(ctrack_zipped)