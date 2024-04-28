import os
import time
from PIL import Image
from django.conf import settings


def saveImage(f):
    static_domain = settings.STATIC_DOMAIN
    image_path = settings.IMAGE_PATH
    baseDir = os.path.dirname(os.path.abspath(__name__))
    dirPath = os.path.join(baseDir, image_path)
    if not os.path.isdir(dirPath):
        os.makedirs(dirPath)
    unique_name = time.strftime("%Y-%m-%d-%H-%M-%S") + f.name
    path = os.path.join(image_path, unique_name)
    pictureDir = os.path.join(baseDir, path)
    print(pictureDir)
    location = static_domain + "/" + image_path + "/" + unique_name
    fileObj = open(pictureDir, "wb")
    for chunk in f.chunks():
        fileObj.write(chunk)
    fileObj.close()
    image = Image.open(f)
    return {
        "src": location,
        "width": image.width,
        "height": image.height,
        "name": f.name,
        "unique_name": unique_name,
    }


def deleteImage(name):
    image_path = settings.IMAGE_PATH
    path = os.path.join(image_path, name)
    os.remove(path)
