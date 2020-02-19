import pygame
import time
import random

pygame.init()
scr=pygame.display.set_mode( (800,600) )

end=0
clock=pygame.time.Clock()

x=400
y=300

while end==0:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			end=1
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_w:
				y-=10
			if event.key==pygame.K_s:
				y+=10
			if event.key==pygame.K_a:
				x-=10
			if event.key==pygame.K_d:
				x+=10

	
	scr.fill( (255,255,255) ) #게임 배경화면
	pygame.draw.rect( scr ,(0,0,0),[x,y,10,10])

	pygame.display.update() #화면 최신화
	clock.tick(30) #1초에 이 코드를 30번 반복

