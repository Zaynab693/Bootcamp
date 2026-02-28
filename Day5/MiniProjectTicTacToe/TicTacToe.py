def display_board(board):
    print("\nTIC TAC TOE")
    print("***************")
    for i in range(3):
        print("*  " + " | ".join(board[i]) + "  *")
        if i < 2:
            print("* ---+---+--- *")
    print("***************")


def player_input(board, player):
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if row in range(3) and col in range(3):
                if board[row][col] == " ":
                    return row, col
                else:
                    print("Cell already taken.")
            else:
                print("Invalid position.")
        except:
            print("Enter numbers only.")


def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_tie(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))


def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to TIC TAC TOE!")

    while True:
        display_board(board)
        print(f"\nPlayer {current_player}'s turn...")

        row, col = player_input(board, current_player)
        board[row][col] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"\nPlayer {current_player} wins!")
            break

        if check_tie(board):
            display_board(board)
            print("\nIt's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


play()