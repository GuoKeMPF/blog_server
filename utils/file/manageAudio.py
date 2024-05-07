import os
import time
from pathlib import Path
from django.conf import settings


def saveAudio(f):
    static_domain = settings.STATIC_DOMAIN
    audio_path = settings.AUDIO_PATH

    baseDir = os.path.dirname(os.path.abspath(__name__))
    dirPath = os.path.join(baseDir, audio_path)
    if not os.path.isdir(dirPath):
        os.makedirs(dirPath)
    unique_name = time.strftime("%Y-%m-%d-%H-%M-%S") + f.name
    path = os.path.join(audio_path, unique_name)
    audioDir = os.path.join(baseDir, path)
    print(audioDir)
    location = static_domain + "/" + audio_path + "/" + unique_name
    fileObj = open(audioDir, "wb")
    for chunk in f.chunks():
        fileObj.write(chunk)
    fileObj.close()
    return {"src": location, "name": f.name, "unique_name": unique_name}


def deleteAudio(name):
    audio_path = settings.AUDIO_PATH
    path = os.path.join(audio_path, name)
    os.remove(path)
