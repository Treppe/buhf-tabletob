import os
from math import ceil
from PIL import Image


PROPORTION_SPIN = 1
PROPORTION_GRAB = 1
PROPORTION_EMPTY = 2

spin = Image.open("spin.png").convert('RGBA')
grab = Image.open("grab.png").convert('RGBA')
i = 0

spin_prop = PROPORTION_SPIN / (PROPORTION_GRAB + PROPORTION_EMPTY + PROPORTION_SPIN)
grab_prop = PROPORTION_GRAB / (PROPORTION_GRAB + PROPORTION_EMPTY + PROPORTION_SPIN)

cards = []

path = 'cards'
files = os.listdir(path)
for file in files:
    if os.path.isfile(os.path.join(path, file)):
        try:
            card = Image.open(os.path.join(path, file), 'r').convert('RGB')
            cards.append(card)
        except Exception as err:
            print(err)
print('aaAAAAa', spin_prop * len(cards))
for card in cards:
    path2save = f'cards/new_cards/new_cards{i}.png'

    if i <= (spin_prop * len(cards)):    
        card.paste(spin, (0, 0), spin)

    elif i <= ((grab_prop * len(cards)) + spin_prop * len(cards)):
        card.paste(grab, (0, 0), grab)

    else:
        pass
    card.save(path2save)
    i += 1
