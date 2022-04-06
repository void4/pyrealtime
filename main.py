import pygame
from time import sleep

pygame.init()
pygame.display.set_caption("my title")

w = 640
h = 480

screen = pygame.display.set_mode((w,h))

color = (0, 0, 0)

i = 0
running = True
while running:
	screen.fill(color)

	#pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(i, i, 40, 30))
	i += 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			print(pos)

	print(pygame.key.get_pressed()[pygame.K_UP])

	pygame.display.flip()
	sleep(0.1)
