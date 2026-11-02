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

	refPack = []


	back_back = pygame.surface.Surface((12*scale, 20*scale))
	back_back.fill(prefs["pieceBorderColor"])



	headHeight = scale*3



	for i in range(2):
		packs[i].append([back_back, [scale*0, scale*-4]])

		packs[i].append([circleSurface(8*scale, prefs["pieceBorderColor"]), [0, headHeight]])


	for i in range(2):
		surf = pygame.surface.Surface((8*scale, 16*scale))
		surf.fill(col[i][1])
		packs[i].append([surf, [scale*0, scale*-3]])

		packs[i].append([circleSurface(6*scale, col[i][0]), [scale*0, headHeight]])




	return packs