import pygame
from circleSurface import circleSurface



def getPacks(prefs):
	scale = 50/prefs["squareSize"]
	col = prefs[""]


	packBlack = []
	packWhite = []

	pack = []



	packBlack.append([circleSurface(15*scale, prefs["black_piece"]), [0, 0]])
	packWhite.append([circleSurface(15*scale, prefs["white_piece"]), [0, 0]])