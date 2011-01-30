#!/usr/bin/env python
import math
from gimpfu import *

def sprite_repeat_layer(img, drw, width = 1, direction = 'h'):
    img.disable_undo()
    layer = img.layers[0]
    h = layer.height
    w = layer.width

    if direction == 'h':
        c = math.ceil(width / layer.width)
    else :
        c = math.ceil(width / layer.height)
    i = c - 1
    while i > 0:
        copy = layer.copy()
        x, y = layer.offsets
        if direction == 'h':
            x += w
        else:
            y += h
        copy.set_offsets(x, y)
        img.add_layer(copy, 0)
        layer = copy
        i -= 1

    x, y = layer.offsets
    if direction == 'h':
        img.resize(x + w, h, 0, 0)
    else:
        img.resize(w, y + h, 0, 0)

    img.merge_visible_layers(CLIP_TO_IMAGE)
    img.enable_undo()

register(
        "sprite_repeat_layer",
        "Ordena las capas por su xy",
        "Ordena las capas por su xy",
        "Loduis Madariaga",
        "Loduis Madariaga",
        "2010",
        "<Image>/Filters/Web/Sprite/Repeat layer",
        "RGBA, RGB",
        [
                (PF_INT, 'width', 'Width:', 1),
                (PF_RADIO, 'direction', 'Build Direction:', 'h', (('Vertical', 'v'), ('Horizontal', 'h')))

        ],
        [],
        sprite_repeat_layer)

main()
