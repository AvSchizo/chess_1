import pygame


from importPieces import getCollection
from piece_pygame_surfaces.circleSurface import circleSurface



def drawPieces(prefs, scrn, state, selected):
	z = prefs["squareSize"]
	pieceCollection = getCollection(prefs)

	for i in range(8):

		for e in range(8):
			
			start = z/2

			la = state[i][e]

			if (la in list(range(10, 16)) or la in list(range(20, 26))) and la in list(pieceCollection.keys()):

				if selected[0] == None:
					wherego = [start+i*z, (8*z-start)-(z*e)]
				elif selected[0][0] == i and selected[0][1] == e:
					wherego = selected[1]
				else:
					wherego = [start+i*z, (8*z-start)-(z*e)]
				
				for ref in pieceCollection[la]:

					surf = ref[0]
				
					rect = surf.get_rect(center=[wherego[0]+ref[1][0], wherego[1]-ref[1][1]])

					scrn.blit(surf, rect)