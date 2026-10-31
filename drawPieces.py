import pygame


from importPieces import getCollection



def drawPieces(prefs, scrn, state):
	z = prefs["squareSize"]
	pieceCollection = getCollection(prefs)

	for a in range(4):

		for e in range(2):
			
			start = z/2
			for i in range(8):
				place = [a*2+e, i]
				la = state[place[0]][place[1]]

				if (la in list(range(10, 15)) or la in list(range(20, 25))) and la in pieceCollection.keys():
					
					ref = pieceCollection[la]

					surf = ref[0]
				
					rect = surf.get_rect(center=[start+i*z+ref[1][0], start+(e*z+a*(z*2))-ref[1][1]])

					scrn.blit(surf, rect)