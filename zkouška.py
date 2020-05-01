import pygame
import random
import time

slozitost = input("Zadejte složitost bludiště (od 5 do 40):")

slozitost = int(slozitost)
while slozitost < 5 or slozitost > 40:
    slozitost = input("Zadej znovu:")
    slozitost = int(slozitost)

# pygame nastavení obrazu
sirka = slozitost * 20 + 80
vyska = slozitost * 20 + 70

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((sirka, vyska))
clock = pygame.time.Clock()
image = pygame.image.load("electronics.png")
pygame.display.set_caption("Robot maze")

robot = pygame.image.load("electronics.png")
robot = pygame.transform.scale(robot, (20, 20))

bg_color = (125, 125, 125)
screen.fill(bg_color)

font = pygame.font.Font("freesansbold.ttf", 18)
text = font.render("End", True, (0, 0, 0), bg_color)
screen.blit(text, (0, 0))
text = font.render("Start", True, (0, 0, 0), bg_color)
screen.blit(text, ((slozitost * 20) + 30, (slozitost * 20) + 20))


# volba proměnných pro bludiště
x = 0
y = 0
w = 20  # tloušťka buňky
grid = []
visited = []
stack = []
solution = {}
robotX = 0
robotY = 0
smer = []

def main():
    # vytvoření mřížky
    def grid_setup(x, y, w):

        for i in range(1, int(slozitost) + 1):  # generuje bludiště 20x20
            x = 20  # zadani x souradnic na zacatek
            y = y + x  # začátek nové řady
            for j in range(1, int(slozitost) + 1):
                # pygame kod
                pygame.draw.line(screen, black, [x, y], [x + w, y])  # vrsek bunky
                pygame.draw.line(screen, black, [x + w, y], [x + w, y + w])  # pravá strana
                pygame.draw.line(screen, black, [x + w, y + w], [x, y + w])  # spodek buňky
                pygame.draw.line(screen, black, [x, y + w], [x, y])  # levá strana buňky
                grid.append((x, y))
                x = x + 20


# pohyby
    def nahoru(x, y):
        pygame.draw.rect(screen, white, (x + 1, y - w + 1, 19, 39), 0)
        pygame.display.update()
        pygame.event.pump()


    def dolu(x, y):
        pygame.draw.rect(screen, white, (x + 1, y + 1, 19, 39), 0)
        pygame.display.update()
        pygame.event.pump()


    def doleva(x, y):
        pygame.draw.rect(screen, white, (x - w + 1, y + 1, 39, 19), 0)
        pygame.display.update()
        pygame.event.pump()


    def doprava(x, y):
        pygame.draw.rect(screen, white, (x + 1, y + 1, 39, 19), 0)
        pygame.display.update()
        pygame.event.pump()


    def bunka_setup(x, y):
        pygame.draw.rect(screen, green, (x + 1, y + 1, 18, 18), 0)
        pygame.display.update()
        pygame.event.pump()


    def backtracking(x, y):
        pygame.draw.rect(screen, white, (x + 1, y + 1, 18, 18), 0)
        time.sleep(0.05)
        pygame.display.update()
        pygame.event.pump()


    def reseni(x, y):
        #screen.blit(robot, (x, y))
        time.sleep(0.1)
        #screen.fill((255, 255, 255), (x + 5, y + 5, 18, 18))
        pocet_kroku = len(smer)
        print(pocet_kroku)
        for i in range(pocet_kroku):
            if i != pocet_kroku - 1:
                p1 = smer[i][0]
                p2 = smer[i + 1][0]

                if i != pocet_kroku - 1 and int(p1) == int(p2):
                    pygame.draw.line(screen, black, [x + 10, y + 10], [x - 10, y + 10], 1)

                if i != pocet_kroku - 1 and int(p1) != int(p2):
                    pygame.draw.line(screen, black, [x + 10, y + 10], [x + 10, y - 20], 1)

                if i == 0 and int(p1) == int(p2):
                    pygame.draw.line(screen, black, [x + 10, y + 10], [x - 10, y + 10], 1)

                if i == 0 and int(p1) != int(p2):
                    pygame.draw.line(screen, black, [x + 10, y + 10], [x + 10, y - 20], 1)

                if i == pocet_kroku and int(p1) == int(p2):
                    pygame.draw.line(screen, black, [x + 10, y + 10], [x + 10, y - 20], 1)

                if i == pocet_kroku and int(p1) != int(p2):
                    pygame.draw.line(screen, black, [x + 10, y + 10], [x - 10, y + 10], 1)

        #fill(x, y)
        pygame.display.update()
        pygame.event.pump()


    def fill(x ,y):
        time.sleep(0.2)
        screen.fill((255, 255, 255), (x + 5, y + 5, 18, 18))
        pygame.display.update()


    # vykreslení bludiště
    def vykresleni(x, y):
        bunka_setup(x, y)  # počátek bludiště
        stack.append((x, y))
        visited.append((x, y))

        while len(stack) > 0:
            time.sleep(.01)
            bunka = []
            if (x + w, y) not in visited and (x + w, y) in grid:
                bunka.append("doprava")
            if (x - w, y) not in visited and (x - w, y) in grid:
                bunka.append("doleva")
            if (x, y + w) not in visited and (x, y + w) in grid:
                bunka.append("dolu")
            if (x, y - w) not in visited and (x, y - w) in grid:
                bunka.append("nahoru")
            if len(bunka) > 0:
                vybrany_smer = random.choice(bunka)
                if vybrany_smer == "doprava":
                    doprava(x, y)
                    solution[(x + w, y)] = x, y
                    x = x + w
                    visited.append((x, y))
                    stack.append((x, y))
                elif vybrany_smer == "doleva":
                    doleva(x, y)
                    solution[(x - w, y)] = x, y
                    x = x - w
                    visited.append((x, y))
                    stack.append((x, y))
                elif vybrany_smer == "nahoru":
                    nahoru(x, y)
                    solution[(x, y - w)] = x, y
                    y = y - w
                    visited.append((x, y))
                    stack.append((x, y))
                elif vybrany_smer == "dolu":
                    dolu(x, y)
                    solution[(x, y + w)] = x, y
                    y = y + w
                    visited.append((x, y))
                    stack.append((x, y))
            else:
                x, y = stack.pop()
                bunka_setup(x, y)
                backtracking(x, y)  # změna barvy na backtracking

    def cesta_zpet(x, y):
        reseni(x, y)
        smer.append((x,y))
        while (x, y) != (20, 20):  # dokud nejsou na počáteční pozici
            x, y = solution[x, y]
            reseni(x, y)
            smer.append((x, y))
        time.sleep(.1)
    x, y = 20, 20  # počáteční pozice mřížky
    grid_setup(20, 20, 20)
    vykresleni(x, y)
    cesta_zpet((20 * slozitost), (20 * slozitost) + 20)


if __name__ == "__main__":
    main()

