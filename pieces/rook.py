from __future__ import annotations

from board_representation import Piece


class Rook(Piece):
    """Blueprint for the rook piece"""

    def __init__(self: Rook, color: int) -> Rook:
        super().__init__(color, 'r')
