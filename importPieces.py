def getSurf(name, t=None):
	surf = pygame.image.load(f"piece_images/{name}").convert_alpha()
	if t == None:
		d = surf.get_width()/50
	else:
		d = t
	surf.subsurface(surf.get_bounding_rect()).copy()
	surf = pygame.transform.scale(surf, [surf.get_width()*d*scale, surf.get_height()*d*scale])
	return surf

def getCollection(prefs):
	pieceCollection = {}

	scale = prefs["squareSize"]/50




	# pawn #
	if prefs["webMode"]["pieces"][5]:
		from piece_pygame_surfaces.pawn import getPacks as pack

		pieceCollection[15], pieceCollection[25] = pack(prefs)
	
	else:
		pieceCollection[15] = [[getSurf("pawn_white.png", .5), [0, 0]]]
		pieceCollection[15] = [[getSurf("pawn_black.png", .5), [0, 0]]]
	#



	# rook #
	if prefs["webMode"]["pieces"][4]:
		from piece_pygame_surfaces.rook import getPacks as pack

		pieceCollection[14], pieceCollection[24] = pack(prefs)
	
	else:
		pieceCollection[14] = [[getSurf("rook_white.png", .5), [0, 0]]]
		pieceCollection[24] = [[getSurf("rook_black.png", .5), [0, 0]]]
	#



	# knight #
	if prefs["webMode"]["pieces"][3]:
		from piece_pygame_surfaces.knight import getPacks as pack

		pieceCollection[13], pieceCollection[23] = pack(prefs)
	
	else:
		pieceCollection[13] = [[getSurf("knight_white.png", .5), [0, 0]]]
		pieceCollection[23] = [[getSurf("knight_black.png", .5), [0, 0]]]
	#



	# bishop #
	if prefs["webMode"]["pieces"][2]:
		from piece_pygame_surfaces.bishop import getPacks as pack

		pieceCollection[12], pieceCollection[22] = pack(prefs)
	
	else:
		pieceCollection[12] = [[getSurf("bishop_white.png", .5), [0, 0]]]
		pieceCollection[22] = [[getSurf("bishop_black.png", .5), [0, 0]]]
	#



	# king #
	if prefs["webMode"]["pieces"][1]:
		from piece_pygame_surfaces.king import getPacks as pack

		pieceCollection[11], pieceCollection[21] = pack(prefs)
	
	else:
		pieceCollection[11] = [[getSurf("king_white.png", .5), [0, 0]]]
		pieceCollection[21] = [[getSurf("king_black.png", .5), [0, 0]]]
	#



	# queen #
	if prefs["webMode"]["pieces"][0]:
		from piece_pygame_surfaces.queen import getPacks as pack

		pieceCollection[10], pieceCollection[20] = pack(prefs)
	
	else:
		pieceCollection[10] = [[getSurf("queen_white.png", .5), [0, 0]]]
		pieceCollection[20] = [[getSurf("queen_black.png", .5), [0, 0]]]
	#
	




	return pieceCollection
