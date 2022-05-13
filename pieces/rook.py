from __future__ import annotations

from logging_module.custom_logging import get_logger
from board_representation.piece import Piece


class Rook(Piece):
    """Blueprint for the rook piece"""

    def __init__(self: Rook, color: int) -> Rook:
        super().__init__(color, 'r')
