import pygame
import random
from math import hypot

pygame.init() #PyGame init
clock=pygame.time.Clock()
pygame.mouse.set_visible(False)

screen=pygame.display.set_mode((1020,661)) #Najava zaslona
pygame.display.set_caption("Moja prva igra") #Ime igre
bg=pygame.image.load("bg.jpg").convert_alpha() #Najava ozadja
font=pygame.font.SysFont(name="Comic sans",size=32) #Najava fonta xd
font2=pygame.font.SysFont(name="Comic sans",size=100) #Najava fonta2 xd
target_pos=(100,100)
pnt=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            a=mouse_pos[0]-target_pos[0]
            b=mouse_pos[1]-target_pos[1]
            h=hypot(a,b)

            if h<=10: #                                                Točke |
                pnt+=3 #                                                     |
                target_pos=(random.randint(30,670),random.randint(30,370)) # |
            elif h<20: #                                                     |
                pnt+=2 #                                                     |
                target_pos=(random.randint(30,670),random.randint(30,370)) # |
            elif h<=30: #                                                    |
                pnt+=1 #                                                     |
                target_pos=(random.randint(30,670),random.randint(30,370)) # |
            else: #                                                          |
                pnt-=2 #                                                     |
                target_pos=(random.randint(30,670),random.randint(30,370)) # V

    screen.blit(bg,(0,0)) #Ozadje na 0,0
    mouse_pos=pygame.mouse.get_pos()
    pygame.draw.circle(screen,"black",target_pos,30) #Nariši tarčo |
    pygame.draw.circle(screen,"white",target_pos,20) #             |
    pygame.draw.circle(screen,"black",target_pos,10) #             V
    target_pos=(target_pos[0]+3,target_pos[1]) #Premik tarče

    pygame.draw.circle(screen,"red",mouse_pos,20,2) #                 Crosshair |
    pygame.draw.line(screen,"red",mouse_pos,(mouse_pos[0],mouse_pos[1]-30),2) # |
    pygame.draw.line(screen,"red",mouse_pos,(mouse_pos[0],mouse_pos[1]+30),2) # |
    pygame.draw.line(screen,"red",mouse_pos,(mouse_pos[0]-30,mouse_pos[1]),2) # |
    pygame.draw.line(screen,"red",mouse_pos,(mouse_pos[0]+30,mouse_pos[1]),2) # V

    text=font.render(f"Točke: {str(pnt)}",True,(0,0,0))
    screen.blit(text,(20,25))

    if pnt<=-5:
        gmover=font2.render("GAME OVER",True,(255,0,0))
        screen.blit(gmover,(210,230))
    if pnt>=10:
        win=font2.render("YOU WIN",True,(255,0,0))
        screen.blit(win,(260,230))

    pygame.display.update() #Next frame, vedno mora biti na koncu
    clock.tick(60) #Razen clock, ker je pač clock Xd