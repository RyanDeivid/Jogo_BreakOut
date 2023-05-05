import pygame
from pygame.locals import *
from sys import exit


def criar_blocos():
    for linha in range(linhas):
        for coluna in range(colunas):
            x = ((padding_left * coluna) + padding_left) + \
                (coluna * bloco_largura)
            y = ((padding_top * linha) + padding_top) + (linha * bloco_altura)
            bloco = pygame.Rect(x, y, bloco_largura, bloco_altura)
            bloco_lista.append(bloco)


pygame.init()

largura = 640
altura = 480
"posição bola"
x_bola = 335
y_bola = 460
"posição prancha"
x_prancha = 300
y_prancha = 467

# blocos
linhas = 4
colunas = 4
bloco_largura = 140
bloco_altura = 40
padding_left, padding_top = 10, 10
bloco_lista = []
criar_blocos()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Breakout")
relogio = pygame.time.Clock()


while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x_prancha = x_prancha - 10
    if pygame.key.get_pressed()[K_d]:
        x_prancha = x_prancha + 10

    prancha = pygame.draw.rect(
        tela, (255, 100, 100), (x_prancha, y_prancha, 70, 10))
    bola = pygame.draw.circle(tela, (255, 255, 255), (x_bola, y_bola), 6)

    for bloco in bloco_lista:
        pygame.draw.rect(tela, (214, 236, 192), bloco)

    pygame.display.update()
