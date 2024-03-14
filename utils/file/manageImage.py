
import os
import time
from PIL import Image

from django.conf import settings


def saveImage(f):
    static_doamin = settings.STATIC_DOAMIN
    image_path = settings.IMAGE_PATH

    baseDir = os.path.dirname(os.path.abspath(__name__))
    if not os.path.isdir(os.path.join(baseDir, image_path)):
        os.makedirs(os.path.join(baseDir, image_path))
    unique_name = time.strftime('%Y-%m-%d %H:%M:%S') + f.name 
    path = os.path.join(image_path, unique_name)
    jpgdir = os.path.join(baseDir, path)
    loaction = static_doamin + '/' + image_path + '/' + unique_name
    fobj = open(jpgdir, 'wb')
    for chrunk in f.chunks():
        fobj.write(chrunk)
    fobj.close()
    image = Image.open(f)
    return {
        'src': loaction,
        'width': image.width,
        'height': image.height,
        'name': f.name,
        'unique_name': unique_name
    }


def deleteImage(name):
    image_path = settings.IMAGE_PATH
    path = os.path.join(image_path, name)
    os.remove(path)
