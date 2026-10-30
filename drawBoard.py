import pygame
pygame.init()

def drawBoard(prefs, scrn):
	z = prefs["squareSize"]

	for a in range(4):

		for e in range(2):

			for i in range(8):

				surf = pygame.surface.Surface([z]*2)
				if i%2 == 0:
					surf.fill(prefs["black_background"])
				else:
					surf.fill(prefs["white_background"])

				scrn.blit(surf, [i*z, 0])