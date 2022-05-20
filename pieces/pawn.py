from __future__ import annotations

from board_representation import Piece

class Pawn(Piece):
    """Blueprint for the pawn piece"""

    def __init__(self: Pawn, color: int) -> Pawn:
        super().__init__(color, 'p')
