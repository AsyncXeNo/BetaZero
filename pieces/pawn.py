from __future__ import annotations

from logging_module.custom_logging import get_logger
from board_representation.piece import Piece


class Pawn(Piece):
    """Blueprint for the pawn piece"""

    def __init__(self: Pawn, color: int) -> Pawn:
        super().__init__(color, 'p')
