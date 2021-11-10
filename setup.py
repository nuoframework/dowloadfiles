# -*- coding: utf-8 -*-

import wget
import shutil

takeurl = input("Inserta la url de descarga del archivo: ")
path = input("Inserte la ruta en la que desa descargar el archivo: ")
url = takeurl

try:    
    wget.download(url, '{path}')
except:
    print("Error")

    

