import os

from multiprocessing import Process
from PIL import Image
import random
import string
import datetime

random.seed(datetime.datetime.now())

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def chunks(l, n):
    n = max(1, n)
    return [l[i:i+n] for i in range(0, len(l), n)]


def resize_image(files, output_dir, width, height, output_name=None, logo=None):
    """
    :param files:
    :param output_dir:
    :param output_name:
    :param width:
    :param height:
    :return:
    """
    for file_ in files:
        image = Image.open(file_)
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

    files = list(map(lambda file: os.path.join(
        BASE_DIR, input_dir, file), os.listdir(input_dir)))

    amount_of_files = len(files) // os.cpu_count()

    chunked_list = chunks(files, amount_of_files)

    processes = [Process(target=resize_image, args=(
        item, output_dir, 2592, 1456, 'result', True)) for item in chunked_list]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
    return


if __name__ == '__main__':
    main()
