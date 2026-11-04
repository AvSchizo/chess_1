import pygame
pygame.init()

import json





# preferences
from savePreferences import savePreferences
from verifyPreferences import verifyPreferences

defaultPreferences = {
	"moving_background": "darkolivegreen3",
	"white_background": "#ebecd0",
	"black_background": "#739552",
	"white_piece_highlight": "#f9f9f9",
	"white_piece": "#dedede",
	"white_piece_shadow": "#d0d0d0",
	"black_piece_highlight": "#a8a6a5",
	"black_piece": "#747271",
	"black_piece_shadow": "#5c5957",
	"squareSize": 100,
	"pieceBorderColor": "black",
	"webMode": True,
}

verifyPreferences(defaultPreferences)

with open("preferences.json", "r") as f:
	preferences = json.load(f)
#





# palettes
def palette_1(prefs):
	prefs["moving_background"] = "#b9ca42"
	prefs["white_background"] = "#ebecd0"
	prefs["black_background"] = "#739552"
	prefs["white_piece_highlight"] = "#f9f9f9"
	prefs["white_piece"] = "#dedede"
	prefs["white_piece_shadow"] = "#d0d0d0"
	prefs["black_piece_highlight"] = "#a8a6a5"
	prefs["black_piece"] = "#747271"
	prefs["black_piece_shadow"] = "#5c5957"
	prefs["pieceBorderColor"] = "black"
	savePreferences(prefs)

def palette_2(prefs):
	prefs["moving_background"] = [170, 190, 150]
	prefs["white_background"] = "#ebecd0"
	prefs["black_background"] = "bisque4"
	prefs["white_piece_highlight"] = "#f9f9f9"
	prefs["white_piece"] = "#dedede"
	prefs["white_piece_shadow"] = "#d0d0d0"
	prefs["black_piece_highlight"] = "#a8a6a5"
	prefs["black_piece"] = "#747271"
	prefs["black_piece_shadow"] = "#5c5957"
	prefs["pieceBorderColor"] = "black"
	savePreferences(prefs)

def palette_3(prefs):
	prefs["moving_background"] = "darkolivegreen3"
	prefs["white_background"] = "#bbbbbb"
	prefs["black_background"] = "#777777"
	prefs["white_piece_highlight"] = "#f9f9f9"
	prefs["white_piece"] = "#dedede"
	prefs["white_piece_shadow"] = "#d0d0d0"
	prefs["black_piece_highlight"] = "#a8a6a5"
	prefs["black_piece"] = "#747271"
	prefs["black_piece_shadow"] = "#5c5957"
	prefs["pieceBorderColor"] = "black"
	savePreferences(prefs)

def palette_4(prefs):
	prefs["moving_background"] = "darkolivegreen3"
	prefs["white_background"] = "#9a9a9a"
	prefs["black_background"] = "#989898"
	prefs["white_piece_highlight"] = "#a4a4a4"
	prefs["white_piece"] = "#a1a1a1"
	prefs["white_piece_shadow"] = "#989898"
	prefs["black_piece_highlight"] = "#a1a1a1"
	prefs["black_piece"] = "#989898"
	prefs["black_piece_shadow"] = "#959595"
	prefs["pieceBorderColor"] = "black"
	savePreferences(prefs)





from drawBoard import drawBoard
from drawPieces import drawPieces


# globals
glos = {
	"font": pygame.font.Font(None, 36),
}

# personal
pers = {
	"side": 2,
	"selected": None,
	"currentFrame": 0,
	"inputs": [],
}


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
glos["board"] = [
	[14,15,0,0,0,0,25,24],
	[13,15,0,0,0,0,25,23],
	[12,15,0,0,0,0,25,22],
	[10,15,0,0,0,0,25,20],
	[11,15,0,0,0,0,25,21],
	[12,15,0,0,0,0,25,22],
	[13,15,0,0,0,0,25,23],
	[14,15,0,0,0,0,25,24],
]



def updateBoard(side):
	new = []





screen = pygame.display.set_mode([preferences["squareSize"]*8]*2)
clock = pygame.time.Clock()
from piece_pygame_surfaces.circleSurface import circleSurface


while True:

	pers["currentFrame"] += 1

	for event in pygame.event.get():

		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
			quit()





	# inputs
	pers["mouseOn"] = pygame.mouse.get_pos()
	while len(pers["inputs"]) < pers["currentFrame"]:

		allAdd = []

		ia = []
		for i, e in enumerate(pers["mouseOn"]):
			p = int(e/preferences["squareSize"])
			ia.append(i*7+(i*-2+1)*p)

		allAdd.append(ia)

		allAdd.append(pygame.mouse.get_pressed())


		pers["inputs"].append(allAdd)





	# make personal copy
	pers["board"] = []

	if pers["side"] == 1:
		## white
		for i in range(8):
			pers["board"].append(glos["board"][i])

	elif pers["side"] == 2:
		## black
		for i in range(8):
			pers["board"].append(list(reversed(glos["board"][7-i])))





	fop = pers["inputs"][pers["currentFrame"]-1]
	foi = pers["inputs"][pers["currentFrame"]-2]


	if fop[1][0] and not foi[1][0] and pers["board"][fop[0][0]][fop[0][1]] != 0:
		# if clicking now but not previous frame
		pers["selected"] = []
		for i in range(2):
			pers["selected"].append(fop[0][i])

	elif not fop[1][0] and pers["selected"] != None:
		# releasing

		pers["board"][fop[0][0]][fop[0][1]] = pers["board"][pers["selected"][0][0]][pers["selected"][0][1]]
		pers["board"][pers["selected"][0][0]][pers["selected"][0][1]] = 0

		pers["selected"] = None


		if pers["side"] == 1:
			for i in range(8):
				t











	screen.fill("lavender")

	drawBoard(preferences, screen, pers["board"], pers["selected"])
	drawPieces(preferences, screen, pers["board"], [pers["selected"], pers["mouseOn"]])






	



	pygame.display.update()

	clock.tick(60)