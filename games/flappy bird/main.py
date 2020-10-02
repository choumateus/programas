import pygame
import neat
import time
import os
import random
largura_da_janela = 600
altura_da_janela = 800

imagens_do_passaro = [pygame.transform.scale2x(pygame.image.load(os.path.join("imagens","passaro1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imagens","passaro2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imagens","passaro3.png")))]
imagem_do_cano = pygame.transform.scale2x(pygame.image.load(os.path.join("imagens","cano.png")))
imagem_do_solo = pygame.transform.scale2x(pygame.image.load(os.path.join("imagens","solo.png")))
imagem_de_fundo = pygame.transform.scale2x(pygame.image.load(os.path.join("imagens","fundo.png")))

class passaro:
    imagens = imagens_do_passaro
    inclinacao_maxima = 25
    velocidade_de_inclinacao =  20
    tempo_da_animacao = 5

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.inclinacao = 0