import pygame
from settings import WHITE

class Player:
	def __init__(self, x, y):
		self.image = pygame.Surface((50, 50))
		self.image.fill(WHITE)
		self.rect = self.image.get_rect(center=(x, y))
		self.speed = 5

	def update(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.rect.y -= self.speed
		if keys[pygame.K_s]:
			self.rect.y += self.speed
		if keys[pygame.K_a]:
			self.rect.x -= self.speed
		if keys[pygame.K_d]:
			self.rect.x += self.speed

	def draw(self, surface):
		surface.blit(self.image, self.rect)
