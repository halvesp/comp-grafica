import pygame

# inicialização do pygame
pygame.init()

# define as dimensões da janela
screen = pygame.display.set_mode((800, 600))

# define o título da janela
pygame.display.set_caption('Desenho de uma Casa com Formas Geométricas')

# cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# função para desenhar a casa
def draw_house(screen):
    # desenha a base da casa (retângulo)
    pygame.draw.rect(screen, BLACK, (200, 300, 400, 200), 2)
    
    # desenha o telhado (triângulo)
    pygame.draw.polygon(screen, BLACK, [(200, 300), (400, 150), (600, 300)], 2)
    
    # desenha a porta (retângulo)
    pygame.draw.rect(screen, BLACK, (370, 400, 60, 100), 2)
    
    # desenhar as janelas (dois retângulos)
    pygame.draw.rect(screen, BLACK, (250, 350, 80, 60), 2)
    pygame.draw.rect(screen, BLACK, (470, 350, 80, 60), 2)
    
    # desenha a árvore (triângulo e retângulo)
    pygame.draw.polygon(screen, BLACK, [(650, 350), (700, 250), (750, 350)], 2)
    pygame.draw.rect(screen, BLACK, (690, 350, 20, 100), 2)
    
    # desenha o sol (círculo)
    pygame.draw.circle(screen, BLACK, (700, 100), 50, 2)
    
    # desenha o vaso de flores (retângulo e triângulo)
    pygame.draw.rect(screen, BLACK, (150, 400, 50, 30), 2)
    pygame.draw.polygon(screen, BLACK, [(150, 400), (175, 370), (200, 400)], 2)
    
    # desenha a flor (círculo e linhas)
    pygame.draw.circle(screen, BLACK, (175, 370), 10, 2)
    pygame.draw.line(screen, BLACK, (175, 360), (175, 380), 2)
    pygame.draw.line(screen, BLACK, (165, 370), (185, 370), 2)
    pygame.draw.line(screen, BLACK, (170, 365), (180, 375), 2)
    pygame.draw.line(screen, BLACK, (180, 365), (170, 375), 2)

# loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # preenche a tela com branco
    screen.fill(WHITE)

    # desenha a casa
    draw_house(screen)

    # atualiza a tela
    pygame.display.flip()

# encerra o pygame
pygame.quit()
