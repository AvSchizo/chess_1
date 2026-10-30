import pygame
pygame.init()





# preferences
from savePreferences import savePreferences
from verifyPreferences import verifyPreferences

defaultPreferences = {
	"white_background": "cream",
	"black_background": "brown",
	"white_piece": "white",
	"black_piece": "black",
}

verifyPreferences(defaultPreferences)

with open("preferences.json", "r") as f:
	preferences = json.load(f)
#

