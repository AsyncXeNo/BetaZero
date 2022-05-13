from __future__ import annotations

from logging_module.custom_logging import get_logger
from board_representation.piece import Piece


class Queen(Piece):
    """Blueprint for the queen piece"""

    def __init__(self: Queen, color: int) -> Queen:
        super().__init__(color, 'q')
