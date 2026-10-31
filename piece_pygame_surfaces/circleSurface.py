import pygame

def circleSurface(radius, color):
	
	surf = pygame.Surface([radius*2]*2, pygame.SRCALPHA)

	pygame.draw.circle(surf, color, [radius]*2, radius)

	return surf