from ImageMap import ImageMap
from Problem import Problem
from GraphSearch import GraphSearch


print "lectura de la imagen"
im = ImageMap(path="Parte 1/mapa.png", blockNum=20)

print "lectura de la imagen finalizada"
im.savePathAsImage()

print "creacion del problema"
pr = Problem(im.pathArray,3,2,1)
print "problema creado"

print "creacion de busqueda"
gs = GraphSearch(1)
print "resultado"
path =  gs.graphSearch(pr)

colorPath = path[1:-1]
im.imageUpdatePath(colorPath)
im.savePathAsImage(path="Parte 1/path.png")

print "finalizado"