from PIL import Image
output_path = r'C:\Users\cemsa\Documents\asdfg\output'
quotes_url = 'https://api.quotable.io/random'
from quote import nameArt, write_quote, Quote
from colors import color_generator
import os


def image_generator(i, im, im_size):
    im1 = Image.new("RGB", im_size, color_generator())
    new_image = Image.new('RGB', ((i + 1) * im_size[0], im_size[1]), (250, 250, 250))
    new_image.paste(im, (0, 0))
    new_image.paste(im1, (im_size[0] * i, 0))
    return new_image


serial_name_pair = {}


def Picasso(j, serial_number):
    im_size_0 = int(2000 / j)
    im_size_1 = 2000

    im = Image.new("RGB", (im_size_0, im_size_1), color_generator())
    im_size = im.size

    i = 1
    while i < j:
        im = image_generator(i, im, im_size)
        i += 1

    new_im = Image.new("RGB", (2000,1000), (0,0,0))
    im.paste(new_im)

    quote = Quote()

    im = write_quote(im, quote.output)
    name_of_the_art = nameArt(serial_number)

    serial_name_pair[serial_number] = name_of_the_art
    serial_name_pair['author'] = quote.author
    serial_name_pair['content'] = quote.content

    completeName = os.path.join(output_path, name_of_the_art + ".png")

    im.save(completeName)
    print(completeName)

    return [name_of_the_art, completeName]
