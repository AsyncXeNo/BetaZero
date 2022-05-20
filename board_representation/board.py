from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union
if TYPE_CHECKING:
    import logging

from logging_module import get_logger
from board_representation import Square, BASE_FEN, COLORS, FILES_INV, PIECES
from board_representation.utils import parse_fen, compile_fen


class Board(object):
    """Mailbox representation of a chess board"""

    def __init__(self: Board, fen: str = BASE_FEN) -> Board:
        self.logger: logging.Logger = get_logger('board')

        self.board_indices: list[int] = [index for index in range(20, 100) if index % 10 != 0 and index % 10 != 9]
        self.squares: list[Square] = [Square(-1, -1, True) if index not in self.board_indices else Square(self.board_indices.index(index) % 8, self.board_indices.index(index) // 8) for index in range(120)]

        self.process_fen(fen)

        self.logger.info('hi! Initialized board')

    def get_square(self: Board, file: int, rank: int) -> Optional[Square]:
        """Returns a square with give file and rank"""

        try:
            return self.squares[self.board_indices[rank * 8 + file]]
        except IndexError:
            self.logger.warning('Attempt to get an invalid square. This should be possible.')

    def get_fen(self: Board) -> str:
        """Returns a FEN string representing the current board state"""

        return compile_fen(self)

    def update_board(self: Board, fen: str) -> None:
        """Updates the board state to a new FEN string"""

        self.process_fen(fen)

    def process_fen(self: Board, fen: str) -> None:
        """Processes the FEN string and sets board attributes accordingly"""

        self.board_info: Optional[dict[str, Union[str, int, dict[str, str]]]] = parse_fen(fen)

        self.turn: int = self.board_info.get('turn')
        self.en_passant_sq: Optional[Square] = self.get_square(FILES_INV[self.board_info.get('eps')[0]] - 1, int(self.board_info.get('eps')[1]) - 1) if self.board_info.get('eps') != '-' else None
        self.castling_info: str = self.board_info.get('castling')
        self.half_move_counter: int = self.board_info.get('hmc')
        self.full_move: int = self.board_info.get('fmn')

        for pos, piece in self.board_info.get('pp').items():
            color = int(piece.isupper())
            self.get_square(int(pos[0]), int(pos[1])).set_piece(PIECES.get(piece.lower())(color))

    def _log_squares(self: Board) -> None:
        """Log all the squares in 10x12 format"""

        output = '\n'

        for rank in range(0, 120, 10):
            for index in range(rank, rank + 10):
                square = self.squares[index]
                if square.sentinel:
                    output += 'XX\t'
                else:
                    output += f'{square}\t'
            output += '\n'

        self.logger.debug(output)

    def _log_squares_with_info(self: Board) -> None:
        """Log all the squares in 10x12 format with additional info"""

        output = '\n'

        for rank in range(0, 120, 10):
            for index in range(rank, rank + 10):
                square = self.squares[index]
                if square.sentinel:
                    output += 'XX:X\t'
                else:
                    output += f'{square}:{square.piece}\t'
            output += '\n'

        self.logger.debug(output)

    def _log_board_info(self: Board) -> None:
        """Logs board information"""

        output = '\n'

        output += f'To move: {COLORS[self.turn]}\n'
        output += f'Half move counter: {self.half_move_counter}\n'
        output += f'Full move number: {self.full_move}\n'
        output += f'En Passant square: {self.en_passant_sq}\n'
        output += f'White Kingside Castling: {"K" in self.castling_info}\n'
        output += f'White Queenside Castling: {"Q" in self.castling_info}\n'
        output += f'Black Kingside Castling: {"k" in self.castling_info}\n'
        output += f'Black Queenside Castling: {"q" in self.castling_info}\n'

        self.logger.debug(output)
