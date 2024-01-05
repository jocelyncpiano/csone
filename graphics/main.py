# import sys module
import sys
import asyncio
import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))

pi=3.14
white = (255,255,255)
screen.fill(white)
black = (0,0,0)

#Background
pygame.draw.rect(screen,(102, 207, 255),(0,0,640,240), 0)
pygame.draw.rect(screen,(97, 219, 64),(0,240,640,240), 0)
# Mountains
pygame.draw.polygon(screen,(89, 75, 65),[(0, 240),(50,240),(25,200)],0)
pygame.draw.polygon(screen,(89, 75, 65),[(25, 240),(145,240),(85,150)],0)

# House Frame
pygame.draw.polygon(screen,(196,136,67),[(320, 195),(205,310),(435,310)],0)
pygame.draw.polygon(screen,(147,184,231),[(320, 210),(220,310),(420,310)],0)
pygame.draw.rect(screen, (147,184,231), (220,310, 200, 100),0)

# Door
pygame.draw.rect(screen, (85,149,199), (245 ,313, 55, 85),0)
pygame.draw.rect(screen, (129,92,53), (252 ,320, 41, 71),0)
pygame.draw.rect(screen, (196,136,67), (261.5 ,328, 22, 55),0)
pygame.draw.rect(screen, (204,204,204), (245, 398, 55, 13),0)

# Window
pygame.draw.rect(screen, (255,255,255), (345, 323, 45, 45),3)
pygame.draw.line(screen, (white) , (345+22.5,323), (345+22,323+45), 3)
pygame.draw.line(screen, (white) , (345,323+22.5), (390,323+22), 3)






# pygame.draw.ellipse(screen, black, (50,50,10,10),0)
# pygame.draw.ellipse(screen, black, (100,50,10,10),0)
# pygame.draw.polygon(screen,(255,0,0),[(80,80),(85,90),(75,90)],0)
# pygame.draw.arc(screen,black,(30,80,100,50),pi,2*pi,2)



# update the screen
pygame.display.update()



# async def main():
#     pygame.draw.ellipse(screen,(black),(50,50,10,10),0)
#     while (True):
#         for event in pygame.event.get() :
#             if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
#                 pygame.quit(); 
#                 sys.exit();


# asyncio.run(main())
