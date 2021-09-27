import random
import math

from main import legal_moves, print_board, score, make_move, opponent, heuristic


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
    def minmax(board, player, is_max, alpha, beta, depth=3):
        opp = opponent(player)

        if depth == 0:
            player_score, opponent_score = score(player, board)
            return (player_score - opponent_score) + heuristic(player, board)

        if is_max:
            value = -math.inf

            for move in legal_moves(player, board):
                # Create the new board.
                temp_board = make_move(move, player, board[:])
                value = max(
                    value, minmax(temp_board, opp, False, alpha, beta, depth - 1))

                if value > beta:
                    break

                alpha = max(alpha, value)

            return value

        else:
            value = math.inf

            for move in legal_moves(player, board):
                # Create the new board.
                temp_board = make_move(move, player, board[:])
                value = min(value,
                            minmax(temp_board, opp, True, alpha, beta, depth - 1))

                if value < alpha:
                    break

                beta = min(beta, value)

            return value

    moves = []

    for move in legal_moves(player, board):
        # Calculate the mini max score.
        minmax_score = minmax(board[:], player, -math.inf, math.inf, True)
        moves.append((minmax_score, move))

    best = max(moves, key=lambda move: move[0])

    return best[1]
