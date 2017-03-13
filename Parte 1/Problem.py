from math import sqrt
class Problem():
    hasError = False
    pathArray = []
    initVal_pos = []
    goalVal = 0
    wallVal = 0
    error = ""

    def __init__(self, array, initVal, goalVal, wallVal):
        self.pathArray = array
        if any(initVal in sublist for sublist in array):
            self.initVal_pos = [[index,row.index(initVal)] for index, row in enumerate(array) if initVal in row][0]
        else:
            self.hasError = True
            self.error = "no se encuentra punto de inicio"
        self.goalVal = goalVal
        self.wallVal = wallVal

    def goalTest(self, position):
        return self.pathArray[position[0]][position[1]] == self.goalVal

    def actions(self, position):
        moves = [1,-1]
        actions = []
        width = len(self.pathArray[0])
        height = len(self.pathArray)
        for move in moves:
            if (0 <= position[0]+move and position[0]+move < height):
                if self.pathArray[position[0]+move][position[1]] != self.wallVal:
                    actions.append([move,0])#movimientos en y
            if (0 <= position[1]+move and position[1]+move < width):
                if self.pathArray[position[0]][position[1]+move] != self.wallVal:
                    actions.append([0,move])#movimientos en x
        return actions
    
    def result(self, position, action):
        return [position[0]+action[0], position[1]+action[1]]
    
    def pathCost(self, path):
        cost = 0
        for i in range(len(path)-1):
            cost += abs(path[i][0]-path[i+1][0]) + abs(path[i][1]-path[i+1][1])
        return cost

    def heuristic1(self, position):
        if not any(self.goalVal in sublist for sublist in self.pathArray):
            return 0
        # = [[index,row.index(self.goalVal)] for index, row in enumerate(self.pathArray) if self.goalVal in row][0]
        
        #return 0.5*(abs(position[0]-searchPos[0])+abs(position[1]-searchPos[1]))
        positions = [[index,row.index(self.goalVal)] for index, row in enumerate(self.pathArray) if self.goalVal in row]
        result = []
        for searchPos in positions:
            result.append(0.5*(abs(position[0]-searchPos[0])+abs(position[1]-searchPos[1])))
        return min(result)
        
        
    def heuristic2(self, position):
        if not any(self.goalVal in sublist for sublist in self.pathArray):
            return 0
        #searchPos = [[index,row.index(self.goalVal)] for index, row in enumerate(self.pathArray) if self.goalVal in row][0]
        #return sqrt((position[0]-searchPos[0])**2+(position[1]-searchPos[1])**2)
        positions = [[index,row.index(self.goalVal)] for index, row in enumerate(self.pathArray) if self.goalVal in row]
        result = []
        for searchPos in positions:
            result.append(sqrt((position[0]-searchPos[0])**2+(position[1]-searchPos[1])**2))
        return min(result)

    

        

    
