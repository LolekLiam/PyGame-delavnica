import pygame
import random

pygame.init() #PyGame init
clock=pygame.time.Clock()
#pygame.mouse.set_visible(False)

screen=pygame.display.set_mode((1000,800)) #Najava zaslona
pygame.display.set_caption("Moja druga igra") #Ime igre

rckt=pygame.image.load("rocket.png").convert_alpha() #Najava rocket
erckt1=pygame.image.load("enemy_rocket.png").convert_alpha() #Najava enemy_rocket1
erckt1=pygame.transform.scale(erckt1,(50,50))
erckt2=pygame.image.load("enemy_rocket2.png").convert_alpha() #Najava enemy_rocket2
erckt2=pygame.transform.scale(erckt2,(50,50))
rckt=pygame.transform.scale(rckt,(30,60))
font=pygame.font.SysFont(name="Comic sans",size=32) #Najava fonta xd
font2=pygame.font.SysFont(name="Comic sans",size=100) #Najava fonta2 xd
target_pos=(100,100)
rckt_x=300
rckt_y=650

e1_x=200
e1_y=0
e1_speed=3

e2_x=300
e2_y=0
e2_speed=2

blt_x=1
blt_y=1
blt_speed=8

while True:
    mouse_pos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if blt_y<0:
                blt_x=mouse_pos[0]+15
                blt_y=rckt_y
    e1_y+=e1_speed
    e2_y+=e2_speed
    if e1_y>800:
        e1_x=random.randint(100,700)
        e1_y=0
        e1_speed=random.randint(2,5)
    if e2_y>800:
        e2_x=random.randint(100,700)
        e2_y=0
        e2_speed=random.randint(2,5)
    screen.fill("black")
    screen.blit(erckt1,(e1_x,e1_y))
    screen.blit(erckt2,(e2_x,e2_y))
    screen.blit(rckt,(mouse_pos[0],rckt_y))
    pygame.draw.circle(screen,"red",(blt_x,blt_y),2)

    pygame.display.update() #Next frame, vedno mora biti na koncu
    clock.tick(60) #Razen clock, ker je pač clock Xd
    