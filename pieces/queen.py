from __future__ import annotations

from board_representation import Piece


class Queen(Piece):
    """Blueprint for the queen piece"""

    def __init__(self: Queen, color: int) -> Queen:
        super().__init__(color, 'q')
