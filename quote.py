from PIL import ImageDraw, ImageFont
import textwrap
import requests
from random_word import RandomWords

quotes_url = 'https://api.quotable.io/random'
from random import randrange
from colors import color_generator


def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=40)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text),
                  line, font=font, fill=text_color)
        y_text += line_height


def nameArt(serial_number):
    while True:
        r = RandomWords()
        name = str(r.get_random_word())
        if name == 'None' or name is None:
            continue
        else:
            break
    outputName = "#" + str(serial_number) + "$" + name
    return outputName


def write_quote(image, quote):
    fontsize = randrange(50, 90)  # starting font size
    font = ImageFont.truetype("arial.ttf", fontsize)
    text_color = color_generator()
    text_start_height = randrange(300)
    draw_multiple_line_text(image, quote, font, text_color, text_start_height)
    return image


class Quote:
    def __init__(self):
        self.q = requests.get(quotes_url)
        self.quote = self.q.json()
        self.output = self.quote["content"] + "   -   " + self.quote["author"]
        self.content = self.quote["content"]
        self.author = self.quote["author"]