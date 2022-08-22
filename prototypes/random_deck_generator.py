import random 

from create_card import create_card

COLORS = ["#88E2CD",
          "#7187E2",
          "#FFD91F",
          "#FF8366"]
NUM_OF_CARDS = 96

deck = []
for i in range(NUM_OF_CARDS):
    first_color_id = random.randint(0, len(COLORS) - 1)
    first_color = COLORS[first_color_id]
    
    colors2 = [color for i, color in enumerate(COLORS) if i != first_color_id]
    second_color_id = random.randint(0, len(colors2) - 1)
    second_color = colors2[second_color_id]
    
    third_color_id = random.randint(0, len(COLORS) - 1)
    third_color = COLORS[third_color_id]
    
    colors4 = [color for i, color in enumerate(COLORS) if i != third_color_id]
    forth_color_id = random.randint(0, len(colors4) - 1)
    forth_color = colors4[forth_color_id]
    
    card = [first_color, second_color, third_color, forth_color]
    deck.append(card)
    
dir2save = "random_deck/"
for i, card in enumerate(deck):
    path2save = dir2save + f"card_{i}.png"
    create_card(card, path2save=path2save)
