from ccodes import rgb_to_hex


class Card():
    def __init__(self, color_map, target_colors):
        self.color_map = [rgb_to_hex(*color) for color in color_map]
        self.color_tracks = self.build_color_tracks(color_map, target_colors)
    
    def build_color_tracks(self, color_map, target_colors):
        color_codes = {}
        for tc_hex in target_colors:
            color_codes[tc_hex] = ""
        
        for color_found in color_map:
            color_found_hex = rgb_to_hex(*color_found)
            
            assert color_found_hex in target_colors
            
            for tc_hex in target_colors:
                if color_found_hex == tc_hex:
                    color_codes[tc_hex] += "1"
                else:
                    color_codes[tc_hex] += "0"
        
        return color_codes