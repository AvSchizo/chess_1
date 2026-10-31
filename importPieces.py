pieceCollection = {}

# pawn #
from piece_pygame_surfaces.pawn import getPacks as pawnPacks

pieceCollection[15], pieceCollection[25] = pawnPacks()
#



# rook #
from piece_pygame_surfaces.pawn import packBlack, packWhite

pieceCollection[14] = packWhite
pieceCollection[24] = packBlack
#



# knight #
from piece_pygame_surfaces.pawn import packBlack, packWhite

pieceCollection[13] = packWhite
pieceCollection[23] = packBlack
#



# bishop #
from piece_pygame_surfaces.pawn import packBlack, packWhite

pieceCollection[12] = packWhite
pieceCollection[22] = packBlack
#



# king #
from piece_pygame_surfaces.pawn import packBlack, packWhite

pieceCollection[11] = packWhite
pieceCollection[21] = packBlack
#



# queen #
from piece_pygame_surfaces.pawn import packBlack, packWhite

pieceCollection[10] = packWhite
pieceCollection[20] = packBlack
#
