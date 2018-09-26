import pygame

file = 'test.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.event.wait()
