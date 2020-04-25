import pygame
from random import randint
import math
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
    window.fill((255,255,255))
    draw_grid(window,500,field)
    for i in layout:
        pygame.draw.rect(window,(255,0,255),(i[0]*field,i[1]*field,field,field))
    pygame.display.update()

def draw_grid(window,screen,field):
    for x in range(0,screen,field):
        pygame.draw.line(window,(0,0,0),(x,0),(x,screen))
        pygame.draw.line(window,(0,0,0),(0,x),(screen,x))

def draw_closed_and_children(window,field,openList,children,closedList,grid):
    window.fill((255,255,255))
    draw_grid(window,500,field)
    draw_blocker(window,grid,field)
    
    for x in openList:
        pygame.draw.rect(window,(0,255,0),(x.position[0]*field,x.position[1]*field,field,field))
        
# =============================================================================
#     for x in children:
#         pygame.draw.rect(window,(255,0,0),(x.position[0]*field,x.position[1]*field,field,field))
# =============================================================================
    
    for x in closedList:
        pygame.draw.rect(window,(128,128,128),(x.position[0]*field,x.position[1]*field,field,field))
    

    pygame.display.update()

def draw_blocker(window,grid,field):
    for x,g in enumerate(grid):
        for k,j in enumerate(g):
            if j ==1:
                pygame.draw.rect(window,(0,0,255),(x*field,k*field,field,field))
        
        
def algorithm(grid,start,end,window,clock,field,startNode,endNode):
    startNode =(int(startNode[0]/field),int(startNode[1]/field))
    startNode =Node(None,startNode)
    endNode =(int(endNode[0]/field),int(endNode[1]/field))
    endNode =Node(None,endNode)
    startNode.gCost = startNode.hCost = startNode.fCost = 0
    endNode.gCost = endNode.hCost = endNode.fCost = 0
    
    openList =[]
    closedList = [] 
    
    openList.append(startNode)
    
    
    while len(openList)>0:
        print('______')
        for i in closedList:
            print(i.position)
        clock.tick(10)

        currentNode = openList[0]
        currentIndex = 0
        for index,item in enumerate(openList):
            if item.fCost < currentNode.fCost:
                currentNode = item
                currentIndex = index
            elif item.fCost == currentNode.fCost:
                if item.hCost < currentNode.hCost:
                    currentNode = item
                    currentIndex = index
        openList.pop(currentIndex)
        
        inclosed = False
        for i in closedList:
            if currentNode.position == i.position:
                inclosed = True
                i.gCost= currentNode.gCost
                i.hCost= currentNode.hCost
                i.fCost= currentNode.fCost
                i.parent = currentNode.parent
                break
        if inclosed ==False:
            closedList.append(currentNode)
        
        if currentNode == endNode:
            path = []
            current = currentNode
            
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]
        
        
        # get all children
        
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
            inclosed = False
            for closed_child in closedList:
                if child == closed_child:
                    inclosed = True
                    break

                
            child.gCost = currentNode.gCost +1
            child.hCost =((child.position[0] - endNode.position[0])**2+(child.position[1]-endNode.position[1])**2)**0.5
            child.fCost = child.gCost + child.hCost
            if inclosed:
                continue
            for openNode in openList:
                if child == openNode and child.gCost > openNode.gCost:
                    continue
            openList.append(child)

        draw_closed_and_children(window,field,openList,children,closedList,grid)

    
def main():
    screen = 500
    cols = 10
    field = int(screen/cols)
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((screen,screen))
    pygame.display.set_caption("Pathfinder")
    grid= [[0 for i in range(cols)] for j in range(cols)]
    
    grids = True
    window.fill((255,255,255))
    startNode = (0,0)
    endNode = (450,450)
    
    gogo = True
    
    while gogo:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                gridpos = pygame.mouse.get_pos()
                gridy = gridpos[0] //field
                gridx = gridpos[1] //field
                grid[gridy][gridx] = 1
                
            if event.type  == pygame.MOUSEBUTTONDOWN and event.button ==3:
                gridpos = pygame.mouse.get_pos()
                gridy = gridpos[0] //field
                gridx = gridpos[1] //field
                grid[gridy][gridx] = 0
                
            window.fill((255,255,255))
            draw_grid(window,screen,field)
            draw_blocker(window, grid, field)
            pygame.draw.rect(window,(0,255,255),(startNode[0],startNode[1],field,field))
            pygame.draw.rect(window,(0,0,0),(endNode[0],endNode[1],field,field))
            pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gogo = False
                    
    layout = algorithm(grid,startNode,endNode,window,clock,field,startNode,endNode)
    draw_path(window, layout, field)
    
if __name__ == '__main__':
    main()
               
            
        
                