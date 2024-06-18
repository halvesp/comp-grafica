import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# inicialização do pygame e definição de parâmetros
pygame.init()
screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Desenhar Pontos com Pygame e OpenGL')

# configuração de câmera
gluOrtho2D(0, 800, 0, 600)

# lista para armazenar os pontos desenhados
points = []

# configurações iniciais
point_size = 5
point_color = (1.0, 1.0, 1.0)

def draw_points(points):
    glPointSize(point_size)
    glBegin(GL_POINTS)
    for point in points:
        glVertex2f(point[0], point[1])
    glEnd()

def draw_reset_button():
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_QUADS)
    glVertex2f(700, 20)
    glVertex2f(780, 20)
    glVertex2f(780, 50)
    glVertex2f(700, 50)
    glEnd()

    # desenha o texto do botão usando pygame
    font = pygame.font.SysFont('Helvetica', 18)
    text_surface = font.render('Reset', True, (0, 0, 0))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glWindowPos2d(710, 25)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

def is_reset_button_clicked(x, y):
    return 700 <= x <= 780 and 20 <= y <= 50

# looping principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            y = 600 - y  # inverte a coordenada y

            if is_reset_button_clicked(x, y):
                points = []
            else:
                points.append((x, y))
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                point_color = (1.0, 0.0, 0.0)  # vermelho
            elif event.key == pygame.K_g:
                point_color = (0.0, 1.0, 0.0)  # verde
            elif event.key == pygame.K_b:
                point_color = (0.0, 0.0, 1.0)  # azul
            elif event.key == pygame.K_UP:
                point_size += 1  # aumenta o tamanho do ponto
            elif event.key == pygame.K_DOWN:
                point_size -= 1  # diminui o tamanho do ponto

    # limpa a tela
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(*point_color)  # cor dos pontos

    # desenha os pontos
    draw_points(points)

    # desenha o botão de reset
    draw_reset_button()

    # atualiza a tela
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
