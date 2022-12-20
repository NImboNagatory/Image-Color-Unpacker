from PIL import Image
from collections import defaultdict


def return_colors(img):
    img = Image.open(img)
    by_color = defaultdict(int)
    for pixel in img.getdata():
        by_color[pixel] += 1
    return (sorted(by_color.items(), key=lambda item: item[1]))[-10:]


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', "TIFF", "PSD", "RAW", "BMP"}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
