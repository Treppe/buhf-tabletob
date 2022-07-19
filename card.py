#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 16:04:16 2022

@author: egor
"""
import numpy as np

class Card():
    def __init__(self, color_map):
        self.color_map = color_map
        self.color_enum = self.build_enum(color_map)
        self.color_codes = self.build_color_codes(color_map, self.color_enum)
    
    def build_enum(self, color_map):
        color_map_copy = list(color_map)
        color_enum = {}
        enum_num = 1
        for i, _ in enumerate(color_map):
            color = color_map_copy.pop(0)
            color_enum[enum_num] = color
            
            pixel_in_list = any((color == other_c).all() 
                                for other_c in color_map_copy)
            if not pixel_in_list:
                enum_num += 1
        
        return color_enum
    
    def build_color_codes(self, color_map, color_enum):
        color_codes = {}

        for num in color_enum.keys():
            color_codes[num] = ""
            for color in color_map:
                if (color == color_enum[num]).all():
                    color_codes[num] += "1"
                else:
                    color_codes[num] += "0"
        
        return color_codes