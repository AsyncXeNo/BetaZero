from __future__ import annotations

from logging_module.custom_logging import get_logger
from board_representation.piece import Piece


class Knight(Piece):
    """Blueprint for the knight piece"""

    def __init__(self: Knight, color: int) -> Knight:
        super().__init__(color, 'n')
