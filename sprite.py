'''
Created on Jul 2, 2010

@author: loduis
'''
def order_layers(img, drw, rows = 1):
  layers = img.layers
  list = []
  for layer in layers:
      copy = layer.copy()
      copy.name = layer.name
      list.append(copy)
      img.remove_layer(layer)
  if rows > 1:
    c = len(list)
    n = int(round(c / rows))
    if n > 1:
      j = 0
      a = 1
      layer = list[j]
      x1, y1 = layer.offsets
      j += 1
      while j < c:
        layer = list[j]
        x2, y2 = layer.offsets
        if y2 != y1:
          layer.set_offsets(x2, y1)
        a += 1
        #termina la linea
        if a == n:
          a = 1
          j += 1
          if j >= c:
            break
          layer = list[j];
          x1, y1 = layer.offsets;
        j += 1;

  i = 0;
  layers = [];
  while True:
      l = len(list)
      layer = list[0]
      if l <= 1:
          layers.append(layer)
          break
      j = 0
      while j < l:
          x1, y1 = layer.offsets
          x2, y2 = list[j].offsets
          ''' miramos el layer
              si la posicion en Y del layer comparada es mayor
              que el que le sigue se cambia de layer dado que este
              esta mas arriba o si tiene igual posicion Y pero 
              tiene X mayor es el mismo caso
          '''
          if  y1 > y2 or (x1 > x2 and y1 == y2):
              layer = list[j]
          j += 1
      layers.append(layer)
      list.remove(layer)

  i = 1
  for layer in layers:
      img.add_layer(layer, i)
      i += 1

