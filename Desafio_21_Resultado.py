# coding=utf-8
# Faça um Programa em Python que abra a reproduz audio de um mp3

# Metodo usando a Biblioteca PyGame .
import pygame
pygame.mixer.init()
pygame.mixer.music.load('GEAZY.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
