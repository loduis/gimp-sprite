#!/usr/bin/env python
from gimpfu import *
import re

'''
============================= 
  funcion general de sprite
=============================
'''
def sprite_remove_extension(img, drw):
  for layer in img.layers:
    layer.name = re.sub(r'(\..*$)', '', layer.name)

'''
============================= 
  registramos el plugin
=============================
'''
register(
  "sprite_remove_extension",
  "Ordena las capas por su xy",
  "Ordena las capas por su xy",
  "Loduis Madariaga",
  "Loduis Madariaga",
  "2010",
  "<Image>/Filters/Web/Sprite/Remove extension",
  "RGBA, RGB",
  [],
  [],
  sprite_remove_extension
)
'''
============================= 
  ejecutando el plugin
=============================
'''
main()
