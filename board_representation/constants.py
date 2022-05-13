from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from board_representation.piece import Piece
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from pieces.pawn import Pawn

# BASE_FEN: str = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
BASE_FEN: str = 'rnb1kbnr/pppp1ppp/8/4p3/6Pq/5P2/PPPPP2P/RNBQKBNR w KQkq - 1 3'

FILES: dict[int, str] = {num: letter for num, letter in enumerate('abcdefgh', 1)}
FILES_INV: dict[str, int] = {letter: num for num, letter in enumerate('abcdefgh', 1)}

COLORS: dict[int, str] = {1: 'w', 0: 'b'}
COLORS_INV: dict[str, int] = {'w': 1, 'b': 0}

PIECES: dict[str, Piece] = {
    'r': Rook,
    'n': Knight,
    'b': Bishop,
    'q': Queen,
    'k': King,
    'p': Pawn
}
PIECES_INV: dict[Piece, str] = {piece: symbol for symbol, piece in PIECES.items()}
