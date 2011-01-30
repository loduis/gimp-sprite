#!/usr/bin/env python
from gimpfu import *;
import re, os, string, sys, os.path, sprite;


'''
============================= 
  busca una capa por su nombre
=============================
'''
def layer_find_by_name(layers, name):
  for layer in layers:
    if  re.sub(r'(\..*$)', '', layer.name) == name:
      return layer
  return False;

'''
============================= 
  hace un clone de la capa
=============================
'''
def layer_clone(img, layer):
  copy = layer.copy();
  name = re.sub(r'(\..*$)', '', layer.name);
  img.remove_layer(layer);
  copy.name = name;
  return copy;

'''
============================= 
  funcion general de sprite
=============================
'''
def sprite_buttons(img, drw, mt = 0, ml = 0, order = False):
  if order:
    sprite.order_layers(img, drw);
  corners = [];#alamacema la parte izquierda y derecha de un boton cuyo sufijos on -left, -right
  backs = [];#alacema las capas que se repiten horizontalmente el sufijo es -back
  left_right = [];#alamacena capas que se deben horientar a la izquierda o a la derecha
  others = [];#otras imagenes que no necesitan horientacion

  width = img.width;

  while len(img.layers) > 0:
    layer = img.layers[0];
    left = layer_clone(img, layer);
    name = left.name;
    #obtenemos la capa mas ancha
    if width < left.width:
      width = left.width;
    #verificando corners    
    if name.endswith('-left') and not name.endswith('-fixed-left'):
      layer = layer_find_by_name(img.layers, name.replace('-left', '-right'));
      if layer:
        right = layer_clone(img, layer);
        corners.append([left, right]);
      else:
        left_right.insert(0, left);
    elif name.endswith('-right') and not name.endswith('-fixed-right'):
      layer = layer_find_by_name(img.layers, name.replace('-right', '-left'));
      if layer:
        right = layer_clone(img, layer);
        corners.append([right, left]);
      else:
        left_right.append(left);
    elif name.endswith('-back'):
      backs.append(left);
    else:
      others.append(left);

  #==================================
  #      fixed corners
  #==================================
  previous = False;
  i = 0;
  y = 0;
  for layer in corners:
    left, right = layer
    x = width - right.width;
    if not previous:
      left.set_offsets(0, 0);
      right.set_offsets(x, 0);
    else:
      x1, y = previous.offsets;
      y += previous.height + mt;
      left.set_offsets(0, y);
      right.set_offsets(x, y);
    i += 1
    img.add_layer(left, i);
    i += 1
    img.add_layer(right, i);
    previous = left;
  #==================================
  #      fixed backs
  #==================================
  if previous:
    y += previous.height + mt;

  for layer in backs:
    layer.set_offsets(0, y);
    i += 1
    img.add_layer(layer, i);
    #buscamos una capa que este sobre el back
    right = layer_find_by_name(left_right, layer.name.replace('-back', '-right'));
    if right:
      layer.scale(width - right.width, layer.height, 0);
      right.set_offsets(width - right.width, y);
      i += 1;
      img.add_layer(right, i);
      left_right.remove(right);
    elif width != layer.width:
      layer.scale(width, layer.height, 0);
    y += layer.height + mt;
  #==================================
  #      left right
  # Estas capas deben ser organizadas
  # a la derecho o a la izquierda del
  # sprite
  #==================================
  for layer in left_right:
    x = 0;
    if layer.name.endswith('-right'):
      x = width - layer.width;
    layer.set_offsets(x, y);
    i += 1
    img.add_layer(layer, i);
    y += layer.height + mt;
  #==================================
  #     OTHERS LAYERS
  #==================================    
  x = 0;
  h = 0;
  while len(others) > 0:
    layer = others[0];
    i += 1;
    img.add_layer(layer, i);
    #el anco de la capa mas su posicion sobre pasa el ancho de la imagen
    if x != 0 and x + layer.width + ml > width:
      x = 0;
      y += h + mt;
      h = 0;
    #fijamos los layer hacia la derecha
    if layer.name.endswith('-fixed-right'):
      x = width - layer.width;

    layer.set_offsets(x, y);
    #capa mas alta
    if h < layer.height:
      h = layer.height;

    #capa con ancho de la imagen
    if x == 0 and width == layer.width:
      y += layer.height + mt;
      h = 0;
    else:
      x += layer.width + ml;


    others.remove(layer);

  y += h;
  img.resize(width, y)


'''
============================= 
  registramos el plugin
=============================
'''
register(
  "sprite_buttons",
  "Ordena las capas por su xy",
  "Ordena las capas por su xy",
  "Loduis Madariaga",
  "Loduis Madariaga",
  "2010",
  "<Image>/Filters/Web/Sprite/Buttons",
  "RGBA, RGB",
  [
    (PF_INT, 'mt', 'Vertical Offset:', 0),
    (PF_INT, 'ml', 'Horizontal Offset:', 0),
    (PF_TOGGLE, 'order', 'Order layer by offset:', False)
   ],
  [],
  sprite_buttons
)
'''
============================= 
  ejecutando el plugin
=============================
'''
main()
