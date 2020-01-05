import pygame
import sys
import random as rd
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class food:
    blink=True
    def init_food(self,body):
        x=rd.randint(0,29)
        y=rd.randint(0,29)
        self.p=point(x*15+25,y*15+25)
        while any([e.x==self.p.x and e.y==self.p.y for e in body]):
            x=rd.randint(0,29)
            y=rd.randint(0,29)
            self.p=point(x*15+25,y*15+25)
    def draw_food(self,scr):
        if self.blink:
            pygame.draw.rect(scr,RED,(self.p.x,self.p.y,15,15),1)
        self.blink=not self.blink
class snake:
    body=[]
    def __init__(self):
        self.score=0
        self.head=point(85,25)
        self.dir=1
        for i in range(1,4):
            self.body.append(point(85-i*15,25))
    def reset(self):
        self.score=0
        self.body.clear()
        self.head=point(85,25)
        self.dir=1
        for i in range(1,4):
            self.body.append(point(85-i*15,25))
    def eat(self,f):
        if self.head.x==f.p.x and self.head.y==f.p.y:
            self.score+=1
            self.body.insert(0,self.body[0])
            f.init_food(self.body)
    def die(self):
        if any([self.head.x==e.x and self.head.y==e.y for e in self.body]):
          return True
        if self.head.x<25 or self.head.y<25 or self.head.x>=475 or self.head.y>=475:
            return True
        return False
    def move(self):
            self.body.insert(0,point(self.head.x,self.head.y))
            self.body.pop()
            if self.dir==1:
                self.head.x+=15
            elif self.dir==2:
                self.head.x-=15
            elif self.dir==3:
                self.head.y-=15
            else:
                self.head.y+=15
    def control(self,key):
        if key==pygame.K_RIGHT and self.dir!=2:
            self.dir=1
        elif key==pygame.K_LEFT and self.dir!=1:
            self.dir=2
        elif key==pygame.K_UP and self.dir!=4:
            self.dir=3
        elif key==pygame.K_DOWN and self.dir!=3:
            self.dir=4
    def draw_snake(self,scr):
        pygame.draw.rect(scr,RED,(self.head.x,self.head.y,15,15),1)
        for i in range(len(self.body)):
            pygame.draw.rect(scr,RED,(self.body[i].x,self.body[i].y,15,15),1)
def main():
    pygame.init()
    font=pygame.font.SysFont('Garuda', 30)
    font2=pygame.font.SysFont('Garuda',15)
    scr=pygame.display.set_mode((500,500))
    pygame.display.set_caption('Snake Game')
    sn=snake()
    f=food()
    f.init_food(sn.body)
    fps=pygame.time.Clock()
    while 1:
        scr.fill((255,255,255))
        score=font2.render('Your score: {}'.format(sn.score),True,GREEN)
        about=font2.render('Developed by Chung',True,GREEN)
        scr.blit(about,(0,475))
        scr.blit(score,(0,0))
        pygame.draw.rect(scr,BLUE,(25,25,450,450),2)
        if not sn.die():
            sn.move()
            sn.eat(f)
            sn.draw_snake(scr)
            f.draw_food(scr)
        else:
            text=font.render('Game Over',True,BLUE)
            text2=font.render('Press Enter to continue',True,BLUE)
            scr.blit(text,(200,250))
            scr.blit(text2,(150,290))
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                sn.control(event.key)
                if event.key==pygame.K_RETURN:
                    sn.reset()
                    f.init_food(sn.body)
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        fps.tick(30)
        pygame.time.delay(100)
if __name__ == "__main__":
    main()