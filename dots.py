import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# inicializa o pygame e define parâmetros
pygame.init()
screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Desenhar Pontos com Pygame e OpenGL')

# configuração da câmera
gluOrtho2D(0, 800, 0, 600)

# lista para armazenar os pontos desenhados
points = []

def draw_points(points):
    glBegin(GL_POINTS)
    for point in points:
        glVertex2f(point[0], point[1])
    glEnd()

# loop 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # adiciona ponto à lista ao clicar com o mouse
            x, y = pygame.mouse.get_pos()
            y = 600 - y  # inverte coordenada y
            points.append((x, y))

    # limpal a tela
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # cor dos pontos (branco)

    # desenha os pontos
    draw_points(points)

    # atualiza a tela
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
