import os
from math import ceil
from PIL import Image


# PROPORTION_SPIN = 30
PROPORTION_GRAB_PERCENT = 33

spin = Image.open("spin.png")
grab = Image.open("grab.png")
i = 0

# spin_prop = int(100/PROPORTION_SPIN)
grab_prop = ceil(100/PROPORTION_GRAB_PERCENT)
# print('ЭТО ТО, ЧЕРЕЗ СКОЛЬКО КАРТОЧЕК БУДУТ ВСТРЕЧАТЬСЯ СПИНЫ И ГРАБЫ СООТВЕТСТВЕННО', grab_prop, spin_prop)

path = 'cards'
files = os.listdir(path)
for file in files:
    if os.path.isfile(os.path.join(path, file)):
        i += 1
        print('ЭТО ИТЕРАЦИЯ', i)
        path2save = f'cards/new_cards/new_cards{i}.png'
        try: 
            card = Image.open(os.path.join(path, file), 'r')
            if i % grab_prop == 0:
                print('КРАТНО', grab_prop, 'СТАВИМ ГРАБ')
                card.paste(grab, (0, 0), grab)
            else:
                card.paste(spin, (0, 0), spin)
            # elif i % spin_prop == 0:
            #     print('КРАТНО', spin_prop, 'СТАВИМ СПИН')
            #     card.paste(spin, (0, 0), spin)
            card.show()
            card.save(path2save)
        except Exception as err:
            print(err)
