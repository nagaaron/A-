# implementing A star algorithm
import random
import pygame

screen_width = 500
field_size = 10
fields = screen_width/field_size

class Spot:
    def __init__(self,i,j):
        self.x = i
        self.y = j
        self.g = ((self.x-0)*2+(self.y-0)**2)**0.5
        self.h = ((self.x-10)*2+(self.y-10)**2)**0.5
        self.f = self.g + self.h
    
    def draw(self,window,c):
        pygame.draw.rect(window,c,(self.x,self.y,fields,fields))

def distance_between_points(point_a,point_b):
    return ((point_a[1]-point_b[1])**2+(point_a[0]+point_b[0])**2)**0.5

def draw_points(liste,window,c):
    window.fill((0,0,0))
    for i in range(0,500,50):
        pygame.draw.line(window,(0,255,0),(0,i),(500,i))
        pygame.draw.line(window,(0,255,0),(i,0),(i,500))
    for i in liste:
        i.draw(window,c)                        

def main_loop():
    start_point = Spot(0,0)
    end_point = Spot(fields-1,fields-1)
    
    open_list = []
    closed_list = []
    
    open_list.append(start_point)
        
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((screen_width,screen_width))
    pygame.display.set_caption("A* Pathfinder")
    
    while len(open_list)>0:

        clock.tick(10)
        
        index  = 0 
        mini = 10000
        draw_points(open_list,window,(255,255,255))
        for k,i in enumerate(open_list):
            if i.f <= mini:
                mini = i.f
                index = k
        closed_list.append(open_list.pop(index))
        print(len(open_list))
        draw_points(closed_list,window,(0,0,255))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
main_loop()      









    
    

