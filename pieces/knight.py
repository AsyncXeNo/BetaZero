from __future__ import annotations

from board_representation import Piece


class Knight(Piece):
    """Blueprint for the knight piece"""

    def __init__(self: Knight, color: int) -> Knight:
        super().__init__(color, 'n')
