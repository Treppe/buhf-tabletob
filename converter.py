import os

import cv2
import openpyxl
import pandas as pd

from card import Card
from openpyxl.styles import PatternFill


def read_colors(colors_path):
    with open(colors_path) as file:
        colors_hex = file.readlines()
        colors_hex = [line.rstrip().lstrip('#') for line in colors_hex]
    
    return colors_hex


def read_card(img_path, target_colors):
    card = cv2.imread(img_path, cv2.COLOR_BGR2RGB)

    height = card.shape[0]
    colors_id = [i * height // 5 for i in range(1, 5)]

    half_width = card.shape[1] // 2
    colors = [card[i, half_width] for i in colors_id]
    
    card_obj = Card(colors, target_colors)
    
    return card_obj


target_colors = read_colors('colors.txt')
cards_dirs = ['../../cards/test_03_08/']
#cards_dirs = ['../../cards/base', '../../cards/rotor', '../../cards/snatch']

cards_pathes = []
for cdir in cards_dirs:
    for file in os.listdir(cdir):
        filename = os.fsdecode(file)
        if filename.endswith(".png"): 
            path = os.path.join(cdir, filename)
            cards_pathes.append(path)
        else:
            continue

print(f"Reading {len(cards_pathes)} cards...")

cards_list = [read_card(path, target_colors) for path in cards_pathes]

tracks_vs_colors = {track : {color : 0 for color in card.color_tracks.keys()} 
                    for card in cards_list
                    for track in card.color_tracks.values()
                    }

for card in cards_list:
    color_tracks = card.color_tracks
    for color, track in color_tracks.items():
        try:
            tracks_vs_colors[track][color] += 1
        except:
            tracks_vs_colors[track]
    
result = pd.DataFrame.from_dict(tracks_vs_colors)
result = result.T
result = result.reindex(['0110', '0101', '1010', '1001', 
                         '0001', '1000', '0100', '0100', '0000'])

result['Tracks total'] = result.sum(axis=1)
result.to_excel('tracks_vs_colors.xlsx')

wb = openpyxl.load_workbook("tracks_vs_colors.xlsx") #path to the Excel file
ws = wb['Sheet1'] #Name of the working sheet


col_id = ['B', 'C', 'D', 'E']
row_id = 1

for col_num, col_letter in enumerate(col_id):
    cell_val = ws[f"{col_letter}{row_id}"].value
    print(cell_val)
    fill_cell = PatternFill(patternType='solid', fgColor=cell_val) 
    ws[f"{col_letter}{row_id}"].fill = fill_cell
wb.save("tracks_vs_colors.xlsx")



