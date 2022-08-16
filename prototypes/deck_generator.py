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
        #print(f"Track {ctrack1} reached its limit.")
        return True
    return False


def are_same_color(ctrack1, ctrack2):
    for char in ctrack1:
        if char != '0'  and char in ctrack2:
            return True
    return False


ctrack_vs_freq_list = [build_ctrack_vs_freq(color, XTRACK_VS_FREQ) 
                       for color in COLORS]
    
deck = []
has_zeros = []
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
                has_zeros.append(ctrack_zipped)
            else:
                deck.append(ctrack_zipped)


# =============================================================================
# ctracks_original = []
# for a_dict in ctrack_vs_freq_list:
#     ctracks_original += [(key, a_dict) for key in a_dict.keys() 
#                          if a_dict[key] != 0]
# ctrack_all_pairs = list(product(has_zeros, ctracks_original))
# 
# can_add_4th_color = []
# color3_added = {ctrack_z: False for ctrack_z in has_zeros}
# for ctrack_z, ctrack_o_dict in ctrack_all_pairs:
#     ctrack_o, a_dict = ctrack_o_dict
#     if (not are_same_color(ctrack_z, ctrack_o) and 
#         not is_exhausted(a_dict, ctrack_o)):
#         ctrack_zipped = zip_ctracks(ctrack_z, ctrack_o)
#         if not(ctrack_zipped is None):
#             print("HI!")
#             a_dict[ctrack_o] -= 1
#                     
#             color3_added[ctrack_z] = True
#             if '0' in ctrack_zipped:
#                 can_add_4th_color.append(ctrack_zipped)
#             else:
#                 deck.append(ctrack_zipped)
# =============================================================================
        
  
# =============================================================================
# cant_add_3d_color = []
# can_add_4th_color = []
# for ctrack_z in can_add_3d_color:
#     built_card = False
#     for i, a_dict in enumerate(ctrack_vs_freq_list):
#         color = str(i + 1)
#         if color in ctrack_z:
#             break
#         
#         for ctrack_o in a_dict.keys():
#             if ctrack_z == '0221' and ctrack_o == '3000':
#                 print("HI")
#             if is_exhausted(a_dict, ctrack_o):
#                 break
#             ctrack_zipped = zip_ctracks(ctrack_z, ctrack_o)
#             if not(ctrack_zipped is None):
#                 print("HI!")
#                 built_card = True
#                 a_dict[ctrack_o] -= 1
#                 
#                 if '0' in ctrack_zipped:
#                     can_add_4th_color.append(ctrack_zipped)
#                 else:
#                     deck.append(ctrack_zipped)
#     if not built_card:
#         cant_add_3d_color.append(ctrack_z)
# =============================================================================
