import pygame
from constants import * 




def main(): 
    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Gunrunner")

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        
        screen.fill("blue") 

        pygame.draw.rect(screen, (139, 69, 19), (0, 576, SCREEN_WIDTH, SCREEN_HEIGHT - 576))
        
        pygame.draw.line(screen, "black", (0, 576), (SCREEN_WIDTH, 576))
        
        pygame.display.flip() 

if __name__ == "__main__":
    main()