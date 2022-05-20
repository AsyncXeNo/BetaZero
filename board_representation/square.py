from __future__ import annotations

from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    import logging

from logging_module import get_logger
from board_representation import Piece, FILES


class Square(object):
    """Class representing a square on the chess board"""

    def __init__(self: Square, file: int, rank: int, sentinel: bool=False) -> Square:
        self.logger: logging.Logger = get_logger('square')

        self.file: int = file
        self.rank: int = rank
        self.piece: Optional[Piece] = None

        self.sentinel: bool = sentinel

    def set_piece(self: Square, piece: Piece) -> None:
        """Sets a piece on the square"""

        self.piece = piece

    def __str__(self: Square) -> str:
        if self.sentinel:
            return 'X'
        return f'{FILES[self.file + 1]}{self.rank + 1}'

    def __repr__(self: Square) -> str:
        return self.__str__()
