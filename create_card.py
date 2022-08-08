from tkinter import Tk, Canvas
from PIL import Image, ImageDraw, ImageGrab


WIDTH = 431
HEIGHT = 857

POINTS_A = [0, 0, WIDTH, 0, 0, HEIGHT/2]
POINTS_B = [0, HEIGHT/2, WIDTH, 0, WIDTH, HEIGHT/2]
POINTS_C = [0, HEIGHT/2, WIDTH, HEIGHT/2, WIDTH, HEIGHT]
POINTS_D = [0, HEIGHT/2, WIDTH, HEIGHT, 0, HEIGHT]

POLYGONS = [POINTS_A, POINTS_B, POINTS_C, POINTS_D]


def read_colors(colors_path):
    with open(colors_path) as file:
        colors_hex = file.readlines()
        colors_hex = [line.rstrip() for line in colors_hex]
    
    return colors_hex


def create_card():
    target_colors = read_colors('colors.txt')

    master = Tk()
    canvas = Canvas(master, width=WIDTH, height=HEIGHT)
    canvas.pack()

    image = Image.new("RGB", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)

    for i, poly in enumerate(POLYGONS):
        canvas.create_polygon(poly, fill=target_colors[i])
        draw.polygon(poly, target_colors[i])

    filename = "test_card.png"
    image.save(filename)

    master.mainloop()


create_card()
