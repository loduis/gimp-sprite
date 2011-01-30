#!/usr/bin/env python
# Author: Chris Mohler
# Copyright 2009 Chris Mohler
# License: GPL v3
# Version 0.2
# GIMP plugin to export layers as PNGs
# Update by: Loduis Madariaga
# Anexo exportacion de la capa activa

from gimpfu import *
import os

gettext.install("gimp20-python", gimp.locale_directory, unicode = True)


def export_layers(img, drw, path, active = False):
	dupe = img.duplicate();
	if active:
		layers = [dupe.active_layer]
	else:
		layers = dupe.layers;
	for layer in layers:
		layer.visible = 0
	for layer in layers:
		layer.visible = 1
		layer.set_offsets(0, 0)
		name = layer.name + ".png"
		fullpath = os.path.join(path, name);
		pdb.file_png_save(dupe, layer, fullpath, name, 0, 9, 1, 1, 1, 1, 1)
	gimp.delete(dupe)


register(
    "python-fu-export-layers",
    "Export Layers as PNG",
    "Export all layers as individual PNG files.",
    "Chris Mohler",
    "Chris Mohler",
    "2009",
    "<Image>/Filters/Web/Sprite/Export Layers",
    "RGBA, RGB",
    [(PF_DIRNAME, "path", "Save PNGs here", os.getcwd()),
		 (PF_TOGGLE, 'active', 'Only active layer', False)
		],
    [],
    export_layers
)

main()

