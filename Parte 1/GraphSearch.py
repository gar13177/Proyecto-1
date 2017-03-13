class GraphSearch():

    type = 0
    def __init__(self, type=0):
        self.type = type

    def removeChoice(self, frontier,problem):
        if self.type == 0:#bfs
            index = frontier.index(min(frontier, key = lambda x: len(x)))
            return index
        elif self.type == 1:#dfs
            index = frontier.index(max(frontier, key = lambda x: len(x)))
            return index
        elif self.type == 2:#a*
            index = frontier.index(min(frontier, key= lambda x: problem.heuristic1(x[-1])))
            return index
        elif self.type == 3:#a*2
            index = frontier.index(min(frontier, key= lambda x: problem.heuristic2(x[-1])))
            return index
        return -1

    
    def graphSearch(self, problem):
        if self.type == 1: return self.gSDFS(problem)
        
        frontier = [[problem.initVal_pos]]
        explored = []
        
        while frontier:
        #while True:
            #print explored
        #if len(frontier):
            index = self.removeChoice(frontier,problem)
            if index == -1: return []
            path = frontier.pop(index)
            s = path[-1]
            
            if s not in explored:
                explored.append(s) 
                if problem.goalTest(s):
                    return path
                
                for a in problem.actions(s):
                    
                    result = problem.result(s,a)

                    if result not in explored:
                        new_path = []
                        new_path.extend(path)
                        new_path.append(result)
                        frontier.append(new_path)
        #else:
            #return []
        return []

    def gSDFS(self,problem):
        frontier = [[problem.initVal_pos]]
        explored = []

        while frontier:
            path = frontier.pop()#saco el primero
            s = path[-1]#ultimo vertice
            if s not in explored:
                explored.append(s)

                if problem.goalTest(s):
                    return path

                for a in problem.actions(s):

                    result = problem.result(s,a)

                    new_path = []
                    new_path.extend(path)
                    new_path.append(result)
                    frontier.append(new_path)

        return []
                
                
