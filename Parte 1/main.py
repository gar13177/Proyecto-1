from ImageMap import ImageMap
from Problem import Problem
from GraphSearch import GraphSearch

def run(imagePath, blockNumber, searchType):
    im = ImageMap(path=imagePath, blockNum=blockNumber)
    #im.savePathAsImage()
    pr = Problem(im.pathArray,3,2,1)
    if pr.hasError:
        return "error: "+str(pr.error)
    gs = GraphSearch(searchType)
    path =  gs.graphSearch(pr)

    colorPath = path[1:-1]
    im.imageUpdatePath(colorPath)
    im.savePathAsImage(path="path.png")
    return "path.png"
