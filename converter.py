#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt

from card import Card


def read_card(img_path):
    card = cv2.imread(img_path, cv2.COLOR_BGR2RGB)
    plt.imshow(card)
    plt.show()

    height = card.shape[0]
    colors_id = [i * height // 5 for i in range(1, 5)]
    colors_id


    half_width = card.shape[1] // 2
    colors = [card[i, half_width] for i in colors_id]
    
    card_obj = Card(colors)
    print(card_obj.color_enum)
    print(card_obj.color_codes)
    

read_card('../../cards/no-corner4.png')



