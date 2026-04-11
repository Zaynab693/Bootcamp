import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    """Game logic for Tic Tac Toe."""
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def display_board(self):
        """Return a string representation of the board (for CLI)."""
        lines = []
        for i, row in enumerate(self.board):
            lines.append(' ' + ' | '.join(row))
            if i < 2:
                lines.append('---+---+---')
        return '\n'.join(lines)

    def make_move(self, row, col):
        """Place current player's mark if cell is empty. Return True if successful."""
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_win(self, player):
        """Return True if the given player has won."""
        b = self.board
        # Rows and columns
        for i in range(3):
            if all(b[i][j] == player for j in range(3)) or all(b[j][i] == player for j in range(3)):
                return True
        # Diagonals
        if all(b[i][i] == player for i in range(3)) or all(b[i][2-i] == player for i in range(3)):
            return True
        return False

    def check_tie(self):
        """Return True if the board is full and no winner."""
        return all(cell != ' ' for row in self.board for cell in row)

    def switch_player(self):
        """Toggle between X and O."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset(self):
        """Reset the game state."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'


class TicTacToeGUI:
    """Graphical Tic Tac Toe using tkinter."""
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.game = TicTacToe()

        # Status label
        self.status_var = tk.StringVar()
        self.update_status()
        tk.Label(root, textvariable=self.status_var, font=('Arial', 14)).grid(row=0, column=0, columnspan=3, pady=10)

        # Board buttons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                btn = tk.Button(root, text=' ', font=('Arial', 24, 'bold'), width=5, height=2,
                                command=lambda row=r, col=c: self.on_click(row, col))
                btn.grid(row=r+1, column=c, padx=5, pady=5)
                self.buttons[r][c] = btn

        # Reset button
        tk.Button(root, text="New Game", command=self.reset_game).grid(row=4, column=0, columnspan=3, pady=10)

    def update_status(self):
        self.status_var.set(f"Player {self.game.current_player}'s turn")

    def on_click(self, row, col):
        if self.game.board[row][col] != ' ':
            return  # Already taken

        # Make the move
        if self.game.make_move(row, col):
            self.buttons[row][col].config(text=self.game.current_player)

            # Check win or tie
            if self.game.check_win(self.game.current_player):
                messagebox.showinfo("Game Over", f"Player {self.game.current_player} wins!")
                self.disable_buttons()
                return
            elif self.game.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.disable_buttons()
                return

            # Switch player and update status
            self.game.switch_player()
            self.update_status()

    def disable_buttons(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(state=tk.DISABLED)

    def enable_buttons(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(state=tk.NORMAL)

    def reset_game(self):
        self.game.reset()
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text=' ', state=tk.NORMAL)
        self.update_status()



def play_cli():
    game = TicTacToe()
    while True:
        print("\n" + game.display_board())
        print(f"Player {game.current_player}'s turn.")

        try:
            row = int(input("Enter row (0,1,2): "))
            col = int(input("Enter column (0,1,2): "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if not game.make_move(row, col):
            print("That cell is already taken or out of range. Try again.")
            continue

        if game.check_win(game.current_player):
            print("\n" + game.display_board())
            print(f"Player {game.current_player} wins!")
            break
        elif game.check_tie():
            print("\n" + game.display_board())
            print("It's a tie!")
            break

        game.switch_player()


if __name__ == "__main__":
    
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()

  