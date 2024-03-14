
import os
import time
from pathlib import Path
from django.conf import settings


def saveAudio(f):
    static_doamin = settings.STATIC_DOAMIN
    audio_path = settings.AUDIO_PATH

    baseDir = os.path.dirname(os.path.abspath(__name__))
    if not os.path.isdir(os.path.join(baseDir, audio_path)):
        os.makedirs(os.path.join(baseDir, audio_path))
    unique_name = time.strftime('%Y-%m-%d %H:%M:%S') + f.name 
    path = os.path.join(audio_path, unique_name)
    jpgdir = os.path.join(baseDir, path)
    loaction = static_doamin + '/' + audio_path + '/' + unique_name
    fobj = open(jpgdir, 'wb')
    for chrunk in f.chunks():
        fobj.write(chrunk)
    fobj.close()
    return {
        'src': loaction,
        'name': f.name,
        'unique_name': unique_name
    }


def deleteAudio(name):
    audio_path = settings.AUDIO_PATH
    path = os.path.join(audio_path, name)
    os.remove(path)
