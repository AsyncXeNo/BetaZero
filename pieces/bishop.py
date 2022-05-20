from __future__ import annotations

from board_representation import Piece


class Bishop(Piece):
    """Blueprint for the bishop piece"""

    def __init__(self: Bishop, color: int) -> Bishop:
        super().__init__(color, 'b')
