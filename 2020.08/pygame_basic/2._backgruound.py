import pygame
import time

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(("My Game"))

# 배경이미지 불러오기
background = pygame.image.load("C:/RealSong/PycharmProjects/RandDice/pygame_basic/background.png")

running = True # 게임이 진행중인가

while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False

    screen.fill((0, 0, 255))
    # screen.blit(background, (0, 0))
    pygame.display.update() # 게임화면을 다시 그리기
pygame.quit()