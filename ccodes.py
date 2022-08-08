def hex_to_rgb(color_hex):
    color_rgb = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
    return color_rgb


def rgb_to_hex(r, g, b):
  return ('{:X}{:X}{:X}').format(b, g, r)