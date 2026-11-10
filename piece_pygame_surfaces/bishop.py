import pygame
from piece_pygame_surfaces.circleSurface import circleSurface



def getPacks(prefs):
	scale = prefs["squareSize"]/50

	col = [
		[
			prefs["white_piece"],
			prefs["white_piece_shadow"],
			prefs["white_piece_highlight"],
		],
		[
			prefs["black_piece"],
			prefs["black_piece_shadow"],
			prefs["black_piece_highlight"],
		],
	]



	packs = [[], []]


	font = pygame.font.Font(prefs["defaultFont"], scale*30)



	headHeight = scale*2



	for i in range(2):
		packs[i].append(font.render(f"{i+1}2", True, "black"))





	return packs
