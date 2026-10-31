import pygame
pygame.init()

import json





# preferences
from savePreferences import savePreferences
from verifyPreferences import verifyPreferences

defaultPreferences = {
	"moving_background": "darkolivegreen3",
	"white_background": "lightgrey",
	"black_background": "bisque4",
	"white_piece": "bisque",
	"black_piece": "black",
	"squareSize": 50,
}

verifyPreferences(defaultPreferences)

with open("preferences.json", "r") as f:
	preferences = json.load(f)
#



from drawBoard import drawBoard
from drawPieces import drawPieces


# 100s are being moved
# 0 in hundreds place is reg
# 10s are white, 20s are black
# in ones place are:
## 0: queen
## 1: king
## 2: bishop
## 3: knight
## 4: rook
## 5: pawn
# straight 0 is empty

# board is organized by [column][row],
# so e7 would be [4][6] ([(fifth column)-1][(seventh row)-1])
board = [
	[14,15,0,0,0,0,25,24],
	[13,15,0,0,0,0,25,23],
	[12,15,0,0,0,0,25,22],
	[10,15,0,0,0,0,25,20],
	[11,15,0,0,0,0,25,21],
	[12,15,0,0,0,0,25,22],
	[13,15,0,0,0,0,25,23],
	[14,15,0,0,0,0,25,24],
]




screen = pygame.display.set_mode([preferences["squareSize"]*8]*2)
clock = pygame.time.Clock()


while True:

	drawBoard(preferences, screen, board)
	drawPieces(preferences, screen)
	



	pygame.display.update()

	clock.tick(60)
