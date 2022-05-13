from logging_module.custom_logging import get_logger
from board_representation.board import Board
from board_representation.constants import BASE_FEN
from board_representation.utils.fen import parse_fen

logger = get_logger(__name__)


def main():
    logger.info('hi!')
    board = Board()
    board._log_board_info()
    board._log_squares_with_info()
    logger.debug(board.get_fen())
    logger.debug(board.get_fen() == BASE_FEN)


if __name__ == '__main__':
    main()
