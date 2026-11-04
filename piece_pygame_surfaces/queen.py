import pygame
from piece_pygame_surfaces.circleSurface import circleSurface



def getPacks(prefs):
	scale = prefs["squareSize"]/50

	col = [
		[
			prefs["white_piece"],
			prefs["white_piece_shadow"],
			prefs["white_piece_highlight"],
		],
		[
			prefs["black_piece"],
			prefs["black_piece_shadow"],
			prefs["black_piece_highlight"],
		],
	]



	packs = [[], []]

	refPack = []


	back_back = pygame.surface.Surface((16*scale, 26*scale))
	back_back.fill(prefs["pieceBorderColor"])



	head1 = pygame.surface.Surface((6*scale, 22*scale))
	head1.fill(prefs["pieceBorderColor"])

	head2 = pygame.surface.Surface((6*scale, 18*scale))
	head2.fill(prefs["pieceBorderColor"])



	headHeight = scale*2



	for i in range(2):
		# back
		packs[i].append([back_back, [scale*0, scale*-10]])

		# head1
		packs[i].append([head1, [scale*0, scale*12]])

		# head2
		packs[i].append([head2, [scale*-5, scale*10]])

		# head3
		packs[i].append([head2, [scale*5, scale*10]])

		# head
		packs[i].append([circleSurface(10*scale, prefs["pieceBorderColor"]), [scale*0, headHeight]])


	for i in range(2):
		# back
		surf = pygame.surface.Surface((12*scale, 22*scale))
		surf.fill(col[i][1])
		packs[i].append([surf, [scale*0, scale*-9]])

		# head1
		surf = pygame.surface.Surface((2*scale, 18*scale))
		surf.fill(col[i][0])
		packs[i].append([surf, [scale*0, scale*12]])
		hi = pygame.surface.Surface((2*scale, 2*scale))
		hi.fill(col[i][2])
		packs[i].append([hi, [scale*0, scale*20]])

		# head2
		surf = pygame.surface.Surface((2*scale, 14*scale))
		surf.fill(col[i][0])
		packs[i].append([surf, [scale*-5, scale*10]])
		packs[i].append([hi, [scale*-5, scale*16]])

		# head3
		packs[i].append([surf, [scale*5, scale*10]])
		packs[i].append([hi, [scale*5, scale*16]])

		# head
		packs[i].append([circleSurface(8*scale, col[i][0]), [scale*0, headHeight]])




	return packs