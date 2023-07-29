import tkinter


class GameEngine:
    def __init__(self):
        self.counter = 1
        self.playerx_turn = True
        self.squares = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.mark_str = 'X'
        self.game_over = False
        self.draw = False



    def validate_move(self, player_input):
        """Returns a boolean True if the chosen square is free"""
        value_at_square = self.squares[int(player_input) - 1]
        if value_at_square == player_input:
            return True



    def mark_square(self, player_input):
        """Marks players chosen square in the game dataframe"""
        self.squares[int(player_input) - 1] = self.mark_str


    def check_result(self):
        """Checks for a draw or win result to the game. Sets game over to True when draw or win detected and sets
        self.draw to True when draw detected"""
        if self.squares[0] != '1' and self.squares[1] != '2' and self.squares[2] != '3' and self.squares[3] != '4' and self.squares[4] != '5' and self.squares[5] != '6' and self.squares[6] != '7' and self.squares[7] != '8' and self.squares[8] != '9':
            self.game_over = True
            self.draw = True

        if self.squares[0] == self.mark_str and self.squares[1] == self.mark_str and self.squares[2] == self.mark_str:
            self.game_over = True
            self.draw = False
        elif self.squares[3] == self.mark_str and self.squares[4] == self.mark_str and self.squares[5] == self.mark_str:
            self.game_over = True
            self.draw = False
        elif self.squares[6] == self.mark_str and self.squares[7] == self.mark_str and self.squares[8] == self.mark_str:
            self.game_over = True
            self.draw = False
        elif self.squares[0] == self.mark_str and self.squares[3] == self.mark_str and self.squares[6] == self.mark_str:
            self.game_over = True
            self.draw = False
        elif self.squares[1] == self.mark_str and self.squares[4] == self.mark_str and self.squares[7] == self.mark_str:
            self.game_over = True
            self.draw = False
        elif self.squares[2] == self.mark_str and self.squares[5] == self.mark_str and self.squares[8] == self.mark_str:
            self.game_over = True
            self.draw = False
        elif self.squares[0] == self.mark_str and self.squares[4] == self.mark_str and self.squares[8] == self.mark_str:
            self.game_over = True
            self.draw = False
        elif self.squares[2] == self.mark_str and self.squares[4] == self.mark_str and self.squares[6] == self.mark_str:
            self.game_over = True
            self.draw = False


    def set_turns(self):
        """Checks which player's turn it is. Sets players icon as mark_str and mark_img. Sets player prompt.
        Increases move counter"""
        if self.counter % 2 != 0:
            self.playerx_turn = False
            self.mark_img = tkinter.PhotoImage('O.png')
            self.mark_str = 'O'
            prompt = tkinter.Label(text="Player O - It's Your Turn", width=30)
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)


        elif self.counter % 2 == 0:
            self.playerx_turn = True
            self.mark_img = tkinter.PhotoImage('X.png')
            self.mark_str = 'X'
            prompt = tkinter.Label(text="Player X - It's Your Turn", width=30)
            prompt.config(font=('Georgia', 16, 'normal'), pady=10)
            prompt.grid(row=1, column=1)
        self.counter += 1









