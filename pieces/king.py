from __future__ import annotations

from board_representation import Piece


class King(Piece):
    """Blueprint for the king piece"""

    def __init__(self: King, color: int) -> King:
        super().__init__(color, 'k')
