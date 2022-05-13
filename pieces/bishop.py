from __future__ import annotations

from logging_module.custom_logging import get_logger
from board_representation.piece import Piece


class Bishop(Piece):
    """Blueprint for the bishop piece"""

    def __init__(self: Bishop, color: int) -> Bishop:
        super().__init__(color, 'b')
