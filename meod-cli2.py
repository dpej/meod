#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import os
import webbrowser
import lib 
import base64
import json
import argparse
#iciar una aplicaion web -> meod-cli.pyc init nameproyect
#export PATH="$PATH:`pwd`/flutter/bin"
#os.system("comando liux")
def img64(name:str,img_str_64:str):
    imgdata = base64.b64decode(img_str_64)
    with open(name, 'wb') as f:
        f.write(imgdata)

parser = argparse.ArgumentParser()
parser.add_argument("-new", "--new", help="Nombre del nuevo componente")
parser.add_argument("-m","--mode",help="open | closed -> para crear un nodo del dom encapsulado o abierto ")
parser.add_argument("-p","--prefix", help="El prefijo de tus componetes , te recomendamos un nombre corto")
args = parser.parse_args()

if args.prefix:
    prefix:str=args.prefix
else:
    prefix="app"

if sys.argv[1]=="init" and sys.argv[2]:
    name_proyect:str=sys.argv[2]
    os.mkdir("{0}/{1}".format(path,name_proyect))
    
    with open("{0}/{1}/meod-core.js".format(path,name_proyect),"w") as f:
        f.write(lib.Core.core)
    with open("{0}/{1}/meod-support-core.js".format(path,name_proyect),"w") as f:
        f.write(lib.Core.coreSupport)

    os.mkdir("{0}/{1}/css".format(path,name_proyect))
    
    with open("{0}/{1}/css/main.scss".format(path,name_proyect),"w") as f:
        f.write(lib.Css.main)
    
    os.mkdir("{0}/{1}/css/components".format(path,name_proyect))
    arch:dict={"_aside.scss":lib.Css.compAside,"_button-float.scss":lib.Css.compButton,"_input.scss":lib.Css.compInput,"_switch.scss":lib.Css.compSwitch}
    for k,v in arch.items():
        with open("{0}/{1}/css/components/{2}".format(path,name_proyect,k),"w") as f:
            f.write(arch[k])

    with open("{0}/{1}/css/_material.scss".format(path,name_proyect),"w") as f:
        f.write(lib.Css.material)

    os.mkdir("{0}/{1}/fonts".format(path,name_proyect))

    os.mkdir("{0}/{1}/layout".format(path,name_proyect))
    os.mkdir("{0}/{1}/mipmap".format(path,name_proyect))
    
    img:dict={"back.png":lib.Img.back,"menuSd.png":lib.Img.menuSd,"menu.png":lib.Img.menuBar,"plus.png":lib.Img.mas}
    for k,v in img.items():
        img64(f'{path}/{name_proyect}/mipmap/{k}',img[k])

    img64("{0}/{1}/mipmap/loader.gif".format(path,name_proyect),lib.Img.loader)
    
    os.mkdir("{0}/{1}/test".format(path,name_proyect))
    
    os.mkdir("{0}/{1}/values".format(path,name_proyect))
    values:dict={"color.js":lib.Values.color,"dimens.js":lib.Values.dimens,"fonts.js":lib.Values.fonts,"icons.js":lib.Values.icons,"strings.js":"","support.js":lib.Values.toolbarSupport,"ux.js":lib.Values.ux}
    for k,v in values.items():
        with open("{0}/{1}/values/{2}".format(path,name_proyect,k),"w") as f:
            f.write(values[k])
    
    with open("{0}/{1}/com-v0.5.2.js".format(path,name_proyect),"w") as f:
            f.write(lib.Fuera.compresor)
    
    with open("{0}/{1}/manifest.js".format(path,name_proyect),"w") as f:
            f.write(lib.Fuera.manifest)
    
    with open("{0}/{1}/LICENCE".format(path,name_proyect),"w") as f:
            f.write(lib.Fuera.licencia)

    with open("{0}/{1}/readme.md".format(path,name_proyect),"w") as f:
            f.write(lib.Fuera.readme)
    with open("{0}/{1}/manual.txt".format(path,name_proyect),"w") as f:
            f.write(lib.Fuera.manual)
    
    meod_json:str=json.dumps({"path":path,"name_proyect":name_proyect})
    with open("{0}/{1}/manifest.js".format(path,name_proyect),"w") as f:
            f.write(lib.Fuera.manifest)
    with open("{0}/{1}/meod-cli.json".format(path,name_proyect),"w") as f:
            f.write(meod_json)
else:
    
    f=open(f"{os.getcwd()}/meod-cli.json","r")
    meod_py =f.read()
    f.close()
    meod_py=json.loads(meod_py)
    if args.new:
        if args.mode=="closed":
            with open(f"{meod_py['path']}/{meod_py['name_proyect']}/" as target: