import pygame


def drawBoard(prefs, scrn, state, selected):
	z = prefs["squareSize"]

	for i in range(8):

		for e in range(8):

			surf = pygame.surface.Surface([z]*2)
			if selected == None:
				prof = [-1]*2
			else:
				prof = selected

			if i == prof[0] and e== prof[1]:
				surf.fill(prefs["moving_background"])

			elif (i+e)%2 == 0:
				surf.fill(prefs["black_background"])
			else:
				surf.fill(prefs["white_background"])


			scrn.blit(surf, [i*z, (7*z)-e*z])





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
