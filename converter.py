#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:39:52 2022

@author: egor
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# In[]
card = cv2.imread('/home/egor/buhf6/cards/no-corner.png', 0)[1:-1]
plt.imshow(card)
plt.show()
