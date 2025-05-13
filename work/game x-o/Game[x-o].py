import os
from player import Player
from board import Board
from menus import Menu

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
class Game:
    def __init__(self):
     self.players = [Player() , Player()]
     self.board = Board()
     self.menu = Menu()
     self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == 1:
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for number , player in enumerate(self.players , start=1):
            print(f"Player {number}, enter your details:")
            player.choose_name()
            player.choose_symbol()
            clear_screen()

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win():
                choice = self.menu.display_endgame_menu()
                if choice == 1:
                    self.reset_game()
                    break
                else:
                    return
            elif self.check_draw():
                print("\n🤝 It's a draw! No winner this time.\n")
                choice = self.menu.display_endgame_menu()
                if choice == 1:
                    self.reset_game()
                    break
                else:
                    return
            else:
                self.switch_player()

    def quit_game(self):
        print("Thanks for playing!")

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn({player.symbol}):")
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1<= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid choice. Please choose a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number 1 and 9.")


    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def reset_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for combo in win_combinations:
            a, b, c = combo
            if self.board.board[a] == self.board.board[b] == self.board.board[c]:
                winner = self.players[self.current_player_index]
                print(f"\n🎉 {winner.name} wins the game with symbol '{winner.symbol}'! 🎉\n")
                self.board.display_board()
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board) and not self.check_win()
    print("It's a draw!")

game = Game()
game.start_game()