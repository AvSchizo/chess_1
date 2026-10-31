import pygame


def drawBoard(prefs, scrn, state):
	z = prefs["squareSize"]

	for a in range(4):

		for e in range(2):

			for i in range(8):
				place = [a*2+e, i]

				surf = pygame.surface.Surface([z]*2)

				if int(state[place[0]][place[1]]/100) == 1:
					surf.fill(prefs["moving_background"])

				elif (i+e)%2 == 1:
					surf.fill(prefs["black_background"])
				else:
					surf.fill(prefs["white_background"])


				scrn.blit(surf, [i*z, (e*z+a*(z*2))])





# if __name__ != "__main__":
# 	quit()


# preferences = {
# 	"white_background": "lightgrey",
# 	"black_background": "brown",
# 	"white_piece": "white",
# 	"black_piece": "black",
# 	"squareSize": 50,
# }

# screen = pygame.display.set_mode([preferences["squareSize"]*8]*2)
# clock = pygame.time.Clock()


# while True:

# 	drawBoard(preferences, screen)



# 	pygame.display.update()

# 	clock.tick(60)
