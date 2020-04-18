import pygame
import random

class Cube:
    
    def __init__(self,x,y,c,r,w):
        self.pos = (x,y)
        self.c = c
        self.r = r
        self.w = w
    def draw(self,window):
        pygame.draw.rect(window,self.c,(self.pos[0],self.pos[1],self.r,self.r))
        
class Area:
    
    def __init__(self,w1):
        
        self.dir = [(1,0),(-1,0),(0,1),(0,-1)]
        self.body = [(w1.pos[0],w1.pos[1])]
    
    def appender(self):
        for i in self.body:
            for j in self.dir:
                if (i[0]+j[0]*10,i[1]+j[1]*10) not in self.body:
                    self.body.append((i[0]+j[0]*40,i[1]+j[1]*40))
        
    def draw (self,window):
        for i in self.body:
            pygame.draw.rect(window,(0,0,255),(i[0],i[1],40,40))
                 
def grid (w,sw,s):
    for i in range(0,sw+s,s):
        pygame.draw.line(w,(0,0,0),(0,i),(sw,i))
        pygame.draw.line(w,(0,0,0),(i,0),(i,sw))
        
def draw(w,w1, w2,arena):
    w.fill((255,255,255))
    w1.draw(w)
    w2.draw(w)
    arena.draw(w)
    
def main():
    screen_width = 400
    scale = 40
    run = True
    
    wurfel1 = Cube(scale*round(random.randint(0,screen_width-scale)/scale),scale*round(random.randint(0,screen_width-scale)/scale),(255,0,0),scale,screen_width)
    wurfel2 = Cube(scale*round(random.randint(0,screen_width-scale)/scale),scale*round(random.randint(0,screen_width-scale)/scale),(0,0,255),scale,screen_width)
    arena = Area(wurfel1)
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((screen_width,screen_width))
    pygame.display.set_caption("Pathfinder")
    while run == True:
        clock.tick(10)
        draw(window,wurfel1,wurfel2,arena)
        
        grid(window,screen_width,scale)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        arena.appender()
main()      