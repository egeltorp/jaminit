import pygame
from settings import *
from player import Player

def main():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption(TITLE)
	clock = pygame.time.Clock()

	player = Player(WIDTH // 2, HEIGHT // 2)
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# Update game objects
		player.update()

		# Draw
		screen.fill(BG_COLOR)
		player.draw(screen)
		pygame.display.flip()

		clock.tick(FPS)

	pygame.quit()

if __name__ == "__main__":
	main()
