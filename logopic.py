import os

import multiprocessing
from PIL import Image
import random
import string

random.seed(123)

queue = multiprocessing.Queue()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def resize_image(input_dir, output_dir, width, height, output_name=None, logo=None):
    """
    :param input_dir:
    :param output_dir:
    :param output_name:
    :param width:
    :param height:
    :return:
    """
    for n, file_ in enumerate(os.listdir(input_dir)):
        teste = os.path.join(BASE_DIR, input_dir, file_)
        print(teste)
        image = Image.open(teste)
        out_name = output_name and '{0}_{1}'.format(
            output_name, n) or '{0}_{1}'.format(file_, n)
        image.thumbnail((width, height), Image.ANTIALIAS)

        if logo:
            logo_img = Image.open(os.path.join(BASE_DIR, 'logo', 'logo.png'))
            logo_img.thumbnail((550, 550), Image.ANTIALIAS)

            # get images size to position a logo
            main_img_box = image.getbbox()
            logo_img_box = logo_img.getbbox()
            box = ((main_img_box[2] - logo_img_box[2]) -
                   40, (main_img_box[3] - logo_img_box[3]) - 30)
            # paste a logo inside a main_image
            image.paste(logo_img, box, mask=logo_img)

        rand_str = ''.join(random.choice(
            string.ascii_lowercase
            + string.ascii_uppercase
            + string.digits)
            for i in range(5))
        outfile = os.path.join(output_dir, '{0}.jpg'.format(rand_str))
        image.save(outfile, 'JPEG')
        print("Marca d'agua acrescentada com sucesso na foto %s " % rand_str)


def main():


    # AddLogo(os.path.join(BASE_DIR, 'input.jpg'), os.path.join(BASE_DIR, 'logo', 'logo.png'), os.path.join(BASE_DIR, 'output.png'))
    input_dir = os.path.join(BASE_DIR, 'photos')
    output_dir = os.path.join(BASE_DIR, 'output')

    resize_image(input_dir, output_dir, 2592, 1456,
                 output_name='result', logo=True)
    return


if __name__ == '__main__':
    main()
