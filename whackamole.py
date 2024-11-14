import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        x,y=0,0

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
       
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
            for i in range(1,641,32):
                pygame.draw.line(screen, (0,0,0), [i, 0], [i, 512])
            for j in range(1,513,32):
                pygame.draw.line(screen, (0,0,0), [0, j], [640, j])

            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.pos==(x,y) or event.pos<=(x+32,y+32) or event.pos>=(x-32,y-32):
                    x=32*random.randrange(0,20)
                    y=32*random.randrange(0,16)

            pygame.display.flip()
            clock.tick(60)
            
           
    finally:
        pygame.quit()



if __name__ == "__main__":
    main()


