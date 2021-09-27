import random

from main import legal_moves, print_board


def user(player, board):
    # Displays the valid moves and asks the user to make a choice.
    board_str = print_board(board)

    print(board_str)

    # Determine the legal moves.
    moves = legal_moves(player, board)
    print('Legal moves:', moves)

    # Aks the user for a move.
    return int(input('Your move: '))


def rand(player, board):
    # Selects a random move from the valid moves.

    # Determine the legal moves.
    moves = legal_moves(player, board)

    # Return a random move.
    return random.choice(moves)


def minimax(player, board):
    # Determines the best move using the minimax algorithm.
    pass
