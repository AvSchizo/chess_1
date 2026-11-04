def getCollection(prefs):
	pieceCollection = {}


	if prefs["webMode"]:

		# pawn #
		from piece_pygame_surfaces.pawn import getPacks as pawn

		pieceCollection[15], pieceCollection[25] = pawn(prefs)
		#



		# # rook #
		# from piece_pygame_surfaces.king import getPacks as rook

		# pieceCollection[14], pieceCollection[24] = rook(prefs)
		# #



		# # knight #
		# from piece_pygame_surfaces.king import getPacks as knight

		# pieceCollection[13], pieceCollection[23] = knight(prefs)
		# #



		# # bishop #
		# from piece_pygame_surfaces.king import getPacks as bishop

		# pieceCollection[12], pieceCollection[22] = bishop(prefs)
		# #



		# king #
		from piece_pygame_surfaces.king import getPacks as king

		pieceCollection[11], pieceCollection[21] = king(prefs)
		#



		# queen #
		from piece_pygame_surfaces.queen import getPacks as queen

		pieceCollection[10], pieceCollection[20] = queen(prefs)
		#
	


	else:
		import pygame
		pygame.init()

		scale = prefs["squareSize"]/50

		def getSurf(name, t=None):
			surf = pygame.image.load(f"piece_images/{name}").convert_alpha()
			if t == None:
				d = surf.get_width()/50
			else:
				d = t
			surf.subsurface(surf.get_bounding_rect()).copy()
			surf = pygame.transform.scale(surf, [surf.get_width()*d*scale, surf.get_height()*d*scale])
			return surf

		# pawn #
		pieceCollection[15] = [[getSurf("pawn_white.png", .5), [0, 0]]]



	return pieceCollection