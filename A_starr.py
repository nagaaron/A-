class Node:
    def __init__(self,parent=None,position=None):
        self.parent = parent
        self.position = position
        self.gCost = 0
        self.hCost = 0
        self.fCost = 0
    def __eq__(self, other):
        return self.position == other.position
        


def algorithm(grid,start,end):
    startNode = Node(None,start)
    startNode.gCost = startNode.hCost = startNode.fCost = 0
    endNode = Node(None,start)
    endNode.gCost = endNode.hCost = endNode.fCost = 0
    
    openList =[]
    closedList = []
    
    openList.append(startNode)
    
    while len(openList)>0:
        currentNode = openList[0]
        currentIndex = 0
        
        for index,item in enumerate(openList):
            if item.fCost < currentNode.fCost:
                currentNode = item
                currentIndex = index
        openList.pop(currentIndex)
        closedList.append(currentNode)
        
        if currentNode == endNode:
            path = []
            current = currentNode
            
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]
        
        children = []
        for new_position in [(0, -1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]:
            node_position =(currentNode.position[0]+new_position[0],currentNode.position[1]+new_position[1])
            
            if node_position[0] > (len(grid)-1) or node_position[0] < 0 or node_position[1]>(len(grid[len(grid)-1])-1) or node_position[1]<0:
                continue
            if grid[node_position[0]][node_postion[1]]!=0:
                continue
            
            new_node = Node(currentNode, node_position)
            children.append(new_node)
        for child in children:
            for closed_child in closedList:
                if child == closed_child:
                    continue
            child.gCost = currentNode.gCost +1
            child.hCost =((child.position[0] - endNode.positions[0])**2+(child.positions[1]-endNode.positions[1])**2)**0.5
            child.fCost = child.gCost + child.hCost
            
            for openNode in openList:
                if child == openNode and child.gCost > openNode.gCost:
                    continue
            openList.append(child)
            
            
def main():
    grid= [
        [0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],]
    startNode = (0,0)
    endNode =(9,9)
    layout = algorithm(grid,startNode,endNode)
   
    print(layout)
if __name__ == '__main__':
    main()
               
            
        
                