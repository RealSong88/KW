import pygame
import time

screen_width = 480
screen_height = 640

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
# 게임 제목
pygame.display.set_caption(("My Game"))

# FPS
clock = pygame.time.Clock()
# 배경이미지 불러오기
background = pygame.image.load("e:/RealSong/documents/PycharmProjects/RandDice/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("e:/RealSong/documents/PycharmProjects/RandDice/pygame_basic/character.png")
character_size  = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height# 화면 세로크기 가장 아래

# 이동할 좌표
to_x = 0
to_y = 0

# 이동할 속도
character_speed = 0.6


running = True # 게임이 진행중인가
while running:
    dt = clock.tick(120) # 게임화면의 초당 프레임 수를 설정

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False

        if event.type == pygame.KEYDOWN: # 키 눌렸는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터 왼쪽
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터 오른쪽
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터 위
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터 아래
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    pygame.display.update() # 게임화면을 다시 그리기
pygame.quit()