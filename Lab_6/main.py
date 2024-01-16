import random


def generate_board():
    board = [['_' for _ in range(5)] for _ in range(5)]

    start_row = 0
    start_col = 0
    board[start_row][start_col] = 'S'

    end_row = 4
    end_col = 4
    board[end_row][end_col] = 'E'

    obstacles = 0
    while obstacles < 3:
        obstacle_row = random.randint(0, 4)
        obstacle_col = random.randint(0, 4)
        if board[obstacle_row][obstacle_col] == '_':
            board[obstacle_row][obstacle_col] = 'X'
            obstacles += 1

    return board, start_row, start_col, end_row, end_col


def print_board(board):
    for row in board:
        print(' '.join(row))


def move_player(board, direction, current_row, current_col):
    new_row, new_col = current_row, current_col

    if direction == 'w' and current_row > 0:
        new_row -= 1
    elif direction == 's' and current_row < len(board) - 1:
        new_row += 1
    elif direction == 'a' and current_col > 0:
        new_col -= 1
    elif direction == 'd' and current_col < len(board[0]) - 1:
        new_col += 1

    if board[new_row][new_col] != 'X':
        if board[new_row][new_col] != 'E':
            board[current_row][current_col] = '_'
        board[new_row][new_col] = 'S'
        return new_row, new_col
    else:
        return current_row, current_col


def main():
    game_board, player_row, player_col, end_row, end_col = generate_board()
    start_row, start_col = player_row, player_col

    while True:
        print("\nSimpleGame:")
        print_board(game_board)
        move = input("\nW-up, S-down, A-left, D- right, Q-exit\n -> ").lower()

        if move in ['w', 's', 'a', 'd']:
            player_row, player_col, = move_player(game_board, move, player_row, player_col)
            if player_row == end_row and player_col == end_col:
                game_board[player_row][player_col] = '#'
                print_board(game_board)
                print("WIN")
                break
        else:
            return False


if __name__ == "__main__":
    main()
