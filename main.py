import pygame

pygame.init()
pygame.display.set_caption("my title")

w = 640
h = 480

clock = pygame.time.Clock()
screen = pygame.display.set_mode((w,h))

fontcache = {}

def loadfont(fontname, size):
	key = (fontname,size)
	if key not in fontcache:
		fontcache[key] = pygame.font.Font(fontname, size)
	return fontcache[key]

def text(xy, text, color=(255,255,255), fontname=pygame.font.get_default_font(), size=12):
	font = loadfont(fontname, size)
	text = font.render(text, True, color)
	screen.blit(text, xy)

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

	text((w//2,h//2), "test")

	print(pygame.key.get_pressed()[pygame.K_UP])

	pygame.display.flip()
	clock.tick(60)
