from __future__ import annotations

from logging_module.custom_logging import get_logger
from board_representation.piece import Piece


class King(Piece):
    """Blueprint for the king piece"""

    def __init__(self: King, color: int) -> King:
        super().__init__(color, 'k')
