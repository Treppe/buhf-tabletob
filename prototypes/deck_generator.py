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

ctrack_vs_freq_list = []
for color in COLORS:
    ctrack_vs_freq = {}
    for x_track, freq in TRACK_VS_FREQ.items():
        color_track = x2color(x_track, color)
        ctrack_vs_freq[color_track] = freq
    ctrack_vs_freq_list.append(ctrack_vs_freq)
        
