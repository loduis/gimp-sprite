#!/usr/bin/env python
from gimpfu import *
import math, re, sprite;

def sprite_simple(img, drawable, s = 1, t = 0, l = 0, dir = 'v', order = False):
    if order:
      sprite.order_layers(img, drawable, s)
    x = 0 #valor actual de x
    y = 0 # valor actual de y
    w = 0 # el ancho de la image
    h = 0 #alto de l layer
    c = 0 # contador
    lh = 0 #alto del layer mas grade
    layers = [];
    if dir == 'h':
        v = 0;
        for layer in img.layers:
            if layer.visible == True:
                v = v + 1;
                layers.append(layer);
        s = int(round(v / s))
    else :
        layers = img.layers;
      
    for layer in layers:
        #eliminamos la extencion del layer
        layer.name = re.sub(r'(\..*$)', '', layer.name)
        # Movemos el layer a la posicion x y
        layer.set_offsets(x, y)

        if s == 1:
          if dir == 'v':
            x = 0
            y += layer.height + t
            if h < y:
              h = y
            if w < layer.width:
              w = layer.width
          else:
            x += layer.width + l
            y = 0
            if h < layer.height:
              h = layer.height
            if w < x:
              w = x
        else:
          c += 1
          x += layer.width + l
          if w < x:
            w = x
          #se debe manter el layer mas grande que sera la posicion
          # del siguiente grupo
          if lh < layer.height:
            lh = layer.height
          #guardamos el maximo ancho de la imagen
          #ajustamos para generar el nuevo grupo
          if c == s:
            y += lh + t
            c = lh = x = 0
          if h < y:
            h = y
    #resize image        
    img.resize(w - l, h - t, 0, 0)

register(
        'sprite_simple',
        'Crea un sprite desde un conjunto de capas importadas',
        'Crea un sprite desde un conjunto de capas importadas',
        'Loduis Madariaga',
        'Loduis Madariaga',
        '2010',
        '<Image>/Filters/Web/Sprite/Simple',
        'RGBA, RGB',
        [
                (PF_INT, 'split', 'Split:', 1),
                (PF_INT, 'vertical', 'Vertical Offset:', 0),
                (PF_INT, 'horizontal', 'Horizontal Offset:', 0),
                (PF_RADIO, 'direction', 'Build Direction:', 'v', (('Vertical', 'v'), ('Horizontal', 'h'))),
                (PF_TOGGLE, 'order', 'Order layers:', False)
        ],
        [],
        sprite_simple)

main()
