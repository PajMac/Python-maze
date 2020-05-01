import funkce
import pygame


funkce.main()
running = True
while running:
    clock = pygame.time.Clock()
    clock.tick(120)
    for event in pygame.event.get():
        pygame.event.pump()
        if event.type == pygame.QUIT:
            running = False