import pygame
from piece_pygame_surfaces.circleSurface import circleSurface



def getPacks(prefs):
	scale = 50/prefs["squareSize"]
	col = prefs[""]


	packWhite = []
	packBlack = []

	pack = []



	packWhite.append([circleSurface(15*scale, prefs["white_piece"]), [0, 0]])
	packBlack.append([circleSurface(15*scale, prefs["black_piece"]), [0, 0]])



	return packWhite, packBlack