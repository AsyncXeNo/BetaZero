from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
if TYPE_CHECKING:
    import logging

from logging_module.custom_logging import get_logger
from board_representation.constants import COLORS_INV, COLORS, FILES, PIECES_INV
if TYPE_CHECKING:
    from board_representation.board import Board


logger: logging.Logger = get_logger('utils.fen')


def compile_fen(board: Board) -> str:
    """Compiles a FEN string for a Board state"""

    pp = ''

    empty = 0

    for rank in range(7, -1, -1):
        for file in range(0, 8):
            if not board.get_square(file, rank).piece:
                empty += 1
            else:
                if empty > 0:
                    pp += str(empty)
                    empty = 0
                pp += PIECES_INV[board.get_square(file, rank).piece.__class__].upper() if board.get_square(file, rank).piece.color else PIECES_INV[board.get_square(file, rank).piece.__class__]

        if empty > 0:
            pp += str(empty)
            empty = 0

        pp += '/'

    pp = pp[:-1]

    turn = COLORS.get(board.turn)
    castling = board.castling_info
    eps = '-' if not board.en_passant_sq else f'{FILES[board.en_passant_sq.file + 1]}{board.en_passant_sq.rank + 1}'
    hmc = str(board.half_move_counter)
    fmn = str(board.full_move)

    fen = ' '.join([pp, turn, castling, eps, hmc, fmn])

    return fen


def parse_fen(fen_string: str) -> Optional[dict[str, Union[str, int, dict[str, str]]]]:
    """Parsed a FEN string into a dictionary with board information
    
    turn - turn
    castling - castling availability
    eps - en passant square
    hmc - half move counter
    fmn - full move number
    pp - piece placement
    """

    info = {}

    fen = fen_string.split(' ')

    piece_placement = {}
    
    file = -1
    rank = 7

    for letter in fen[0]:
        try:
            file += int(letter)
            if (file > 7):
                logger.error(f'invalid FEN string: pp: {fen}')
                return

        except ValueError:
            if letter == '/':
                file = -1
                rank -= 1

            else:
                file += 1
                piece_placement[f'{file}{rank}'] = letter

    info['pp'] = piece_placement

    try:
        info['turn'] = int(COLORS_INV[fen[1]])
    except KeyError:
        logger.error(f'invalid FEN string: turn: {fen}')
        return

    info['castling'] = fen[2]
    info['eps'] = fen[3]

    try:
        info['hmc'] = int(fen[4])
    except ValueError:
        logger.error(f'invalid FEN string: hmc: {fen}')
        return

    try:
        info['fmn'] = int(fen[5])
    except ValueError:
        logger.error(f'invalid FEN string: fmn: {fen}')
        return

    return info
