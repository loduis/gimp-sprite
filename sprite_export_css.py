#! /usr/bin/env python
from gimpfu import *
import os, string, sys
import os.path


def sprite_export_css(image, drw, path):
  css = ''
  for layer in image.layers:
      x, y = layer.offsets
      if x == 0 :
          l = '0'
      elif image.width == layer.width + x:
          l = '100%'# ES IGUAL A RIGHT PERO TIENE UN BY MENOS 4 VS 5
      else :
          l = "%spx" % (-x)
      if y == 0:
          t = '0'
      else:
          t = "%spx" % (-y)
      css = css + "." + layer.name + "{\n  "
      if layer.name.endswith('-back'):
          css = css + 'background-repeat: repeat-x;' + "\n  "
      css = css + "background-position: %s %s;\r" % (l, t)
      if l == 'right':
          css = css + "  background-position: %spx %s;\r" % (-x, t)
      css = css + "  width: %spx;\n" % (layer.width)
      css = css + "  height: %spx;\n" % (layer.height)
      css = css + "}\n\n"

  fullpath = image.name.replace('xcf', 'css')
  fullpath = os.path.join(path, fullpath);
  file = open(fullpath, 'w')
  file.write(css)
  file.close()

register(
  'sprite_export_css',
  'Genera el css necesario para el sprite',
  'Genera el css necesario para el sprite',
  'Loduis Madariaga',
  'Loduis Madariaga',
  '2010',
  '<Image>/Filters/Web/Sprite/Export css',
  'RGBA, RGB',
  [(PF_DIRNAME, "path", "Save PNGs here", os.getcwd())],
  [],
  sprite_export_css
)

main()
