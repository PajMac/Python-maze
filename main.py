import zkouška
import pygame


zkouška.main()
running = True
while running:
    for event in pygame.event.get():
        pygame.event.pump()
        if event.type == pygame.QUIT:
            running = False