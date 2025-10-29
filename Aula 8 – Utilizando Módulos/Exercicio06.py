#   Faça um programa em Python que abre e reproduza o audio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('Exercicio06.mp3')
pygame.mixer.music.play()
pygame.event.wait()