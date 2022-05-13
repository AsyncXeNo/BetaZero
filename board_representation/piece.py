from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import logging

from logging_module.custom_logging import get_logger


class Piece(object):
    """Blueprint for a chess Piece. Cannot be used on it's own."""

    def __init__(self: Piece, color: int, symbol: str) -> Piece:
        self.logger: logging.Logger = get_logger('piece')

        self.color: int = color
        self.symbol: str = symbol

    def __str__(self: Piece) -> str:
        return self.symbol if not self.color else self.symbol.upper()
