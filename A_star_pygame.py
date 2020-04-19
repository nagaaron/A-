import pygame
class Node:
    def __init__(self,parent=None,position=None):
        self.parent = parent
        self.position = position
        self.gCost = 0
        self.hCost = 0
        self.fCost = 0
    def __eq__(self, other):
        return self.position == other.position

def draw_path(window,layout,field):
    for i in layout:
        pygame.draw.rect(window,(255,0,255),(i[0]*field,i[1]*field,field,field))
    pygame.display.update()
def algorithm(grid,start,end,window,clock):
    startNode = Node(None,start)
    startNode.gCost = startNode.hCost = startNode.fCost = 0
    endNode = Node(None,end)
    endNode.gCost = endNode.hCost = endNode.fCost = 0
    
    openList =[]
    closedList = []
    
    openList.append(startNode)
    window.fill((255,255,255))
    
    while len(openList)>0:
        clock.tick(1)

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
        
        for new_position in [( 0, -1),( 0, 1 ),( -1 ,0),( 1 ,0),( -1 ,-1 ),( -1 , 1 ),( 1 , -1 ),( 1 , 1 )]:
            node_position = (currentNode.position[0]+new_position[0],currentNode.position[1]+new_position[1])
            
            if node_position[0] > (len(grid)-1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid)-1])-1) or node_position[1]<0:
                continue
            if grid[node_position[0]][node_position[1]]!=0:
                continue
            
            new_node = Node(currentNode, node_position)
            
            children.append(new_node)
     
        for child in children:
            for closed_child in closedList:
                if child == closed_child:
                    continue
            child.gCost = currentNode.gCost +1
            child.hCost =((child.position[0] - endNode.position[0])**2+(child.position[1]-endNode.position[1])**2)**0.5
            child.fCost = child.gCost + child.hCost
            
            for openNode in openList:
                if child == openNode and child.gCost > openNode.gCost:
                    continue
            openList.append(child)
        for x in range(0,500,50):
            pygame.draw.line(window,(0,0,0),(x,0),(x,500))
            pygame.draw.line(window,(0,0,0),(0,x),(500,x))
        for x in closedList:
            pygame.draw.rect(window,(128,128,128),(x.position[0]*50,x.position[1]*50,50,50))
        pygame.display.update()
        for x in openList:
            pygame.draw.rect(window,(0,255,255),(x.position[0]*50,x.position[1]*50,50,50))
        pygame.display.update()
    draw_path(window, layout, field)
    for x in range(0,500,50):
        pygame.draw.line(window,(0,0,0),(x,0),(x,500))
        pygame.draw.line(window,(0,0,0),(0,x),(500,x))
    for x in closedList:
        pygame.draw.rect(window,(128,128,128),(x.position[0]*50,x.position[1]*50,50,50))
    pygame.display.update()
    for x in openList:
        pygame.draw.rect(window,(0,255,255),(x.position[0]*50,x.position[1]*50,50,50))
    pygame.display.update()
def main():
    screen = 500
    cols = 10
    field = screen/cols
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((screen,screen))
    pygame.display.set_caption("Pathfinder")

    
    grid= [[0 for i in range(cols)] for j in range(cols)]   
    
    startNode = (0,0)
    endNode =(8,9)
    
    layout = algorithm(grid,startNode,endNode,window,clock)
    draw_path(window, layout, field)

    
   
if __name__ == '__main__':

    main()
               
            
        
                