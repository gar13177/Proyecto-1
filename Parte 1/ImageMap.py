from PIL import Image
from collections import Counter
import numpy


class ImageMap():
    """Clase para discretizar una imagen"""
    imgOriginal = None#pixelAccess con los pixeles originales
    rgbArray = None
    pathArray = []#matriz discretizada
    blockNum = 0#numero de bloques para la division (siempre toma la cantidad para min(width, height))
    colors = {
        "blue": 4,
        "red": 3,
        "green": 2,
        "black": 1,
        "white": 0
        }#diccionario de colores
    colorsValue = {
        "blue": (0, 0, 255, 255),
        "red": (255, 0, 0, 255),
        "green": (0, 255, 0, 255),
        "black": (0, 0, 0, 255),
        "white": (255, 255, 255, 255)
        }

    def __init__(self, blockNum=None, imgOriginal=None, path=None):
        if (imgOriginal != None):
            self.imgOriginal = imgOriginal
        elif (path != None):
            self.setImageByReference(path)

        if (blockNum != None):
            self.setBlockNum(blockNum)
        

    def setImageByReference(self, path):
        """abre una imagen y la guarda como una matriz rgb por medio del nombre"""
        self.imgOriginal = Image.open(path)#carga la imagen
        print self.imgOriginal.format, self.imgOriginal.size, self.imgOriginal.mode
        self.rgbArray = self.imgOriginal.load()

    def setBlockNum(self, blockNum):
        if self.imgOriginal != None:
            reference = min(self.imgOriginal.size)#toma la menor distancia (width, height)
            if blockNum < reference:
                self.blockNum = blockNum
            else:
                blockNum = reference
        self.buildPathArray()

    def getBestColor( self, array):
        colors = []
        for j in range(len(array)):
            x_arr = []
            for i in range(len(array[j])):
                x_arr.append(self.classify(array[j][i]))
            colors.append(x_arr)
        color = max(colors, key = colors.count)
        return self.colors.get(color[0])
        

    def classify(self, rgb_tuple):
        colors = self.colorsValue
        manhattan = lambda x,y : abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2]) 
        distances = {k: manhattan(v, rgb_tuple) for k, v in colors.items()}
        color = min(distances, key=distances.get)
        return color

    def getArrayArea(self, x, y, width, height):
        array = []
        for j in range(y, y+height, 1):
            x_arr = []
            for i in range(x, x+width, 1):
                x_arr.append(self.rgbArray[i, j])
            array.append(x_arr)
        return array

    def buildPathArray(self):
        """construye la matriz a utilizar para buscar los caminos"""
        if self.imgOriginal != None:
            y_init = 0
            step = int(float(min(self.imgOriginal.size))/self.blockNum)
            print "tamano de paso: "+str(step)
            pathArray = []
            while (y_init + step <= self.imgOriginal.size[1]):#se recorre la imagen de arriba hacia abajo
                x_new = []
                x_init = 0
                while (x_init + step <= self.imgOriginal.size[0]):#se recorre de izquierda a derecha
                    array = self.getArrayArea(x_init, y_init,step, step)
                    x_new.append(self.getBestColor(array))
                    x_init += step
                pathArray.append(x_new)
                y_init += step
            
            self.pathArray = pathArray

    def getColor(self, value):
        if value == 4: return (0, 0, 255, 255)
        if value == 3: return (255, 0, 0, 255)
        if value == 2: return (0, 255, 0, 255)
        if value == 1: return (0, 0, 0, 255)
        return (255, 255, 255, 255)

    def savePathAsImage(self, path="path.png"):
        im = Image.new('RGBA',self.imgOriginal.size)
        array = im.load()
        reference = min(self.imgOriginal.size)/self.blockNum
        for j in range(im.size[1]-im.size[1]%reference):
            for i in range(im.size[0]-im.size[0]%reference):
                array[i,j] = self.getColor(self.pathArray[j/reference][i/reference])
        im.save(path)

    def imageUpdatePath(self, path):
        for val in path:
            self.pathArray[val[0]][val[1]] = self.colors.get("blue")

