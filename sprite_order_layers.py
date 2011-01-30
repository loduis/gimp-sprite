#!/usr/bin/env python
from gimpfu import *
import math, sprite;

register(
        "sprite_order_layers",
        "Ordena las capas por su xy",
        "Ordena las capas por su xy",
        "Loduis Madariaga",
        "Loduis Madariaga",
        "2010",
        "<Image>/Filters/Web/Sprite/Order layers by offset",
        "RGBA, RGB",
        [(PF_INT, "rows", "Rows:", 1)],
        [],
        sprite.order_layers)

main()
