import tkinter

# TODO: remove available squares outside the board in the find_available_squares method.
# Alternate the command of the buttons from click to play

#[[ '♖',  '♘',  '♗',  '♕',  '♔',  '♗',  '♘',  '♖'], 
# [ '♙',  '♙',  '♙',  '♙',  '♙',  '♙',  '♙',  '♙'], 
# [None, None, None, None, None, None, None, None], 
# [None, None, None, None, None, None, None, None], 
# [None, None, None, None, None, None, None, None], 
# [None, None, None, None, None, None, None, None], 
# [ '♟︎',  '♟︎',  '♟︎',  '♟︎',  '♟︎',  '♟︎',  '♟︎',  '♟︎'], 
# [ '♜',  '♞',  '♝',  '♛',  '♚',  '♝',  '♞',  '♜']]

class Chess:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.resizable(0,0)

        self.board = []
        
        self.pieces = [["♔", "♕", "♖", "♗", "♘", "♙"], ["♚", "♛", "♜", "♝", "♞", "♟︎"]]
        self.current_player_pieces = self.pieces[0]
        self.current_piece = None

        self.available_squares = []        
        self.previous_available_squares = []
        
        self.knight_available = [
            [-2, -1], [-2, 1], [-1, -2], [-1, 2],
            [2, -1],   [2, 1],   [1, 2], [1, -2]
        ]
        
        self.queen_available = []

        self.king_available = [
            [1, -1],   [1, 0],  [1, 1],  [0, 1], 
            [0, -1], [-1, -1], [-1, 0], [-1, 1]
        ]

        self.bishop_available = []
        
        self.rook_available = []

        self.pawn_available = [[1, 0]] # Implement en-passant and two steps on first move        
        
        for row in range(8):
            if row == 0:
                self.board.append(["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"])
            elif row == 1:
                self.board.append(["♙" for i in range(8)])
            elif row == 6:
                self.board.append(["♟︎" for i in range(8)])
            elif row == 7:
                self.board.append(["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"])
            else:
                self.board.append([None for i in range(8)])
        
        self.squares = [[tkinter.Button(self.window) for row in range(8)] for column in range(8)]
        
        for row in range(8):
            for column in range(8):
                self.squares[row][column].config(
                    height=2, width=4, text=self.board[row][column],
                    background="#588bb6" if (row+column) % 2 == 0 else "#babcbf", 
                    font=("Times 20"), command=lambda 
                    row=row, column=column: self.click(row, column)
                )

                self.squares[row][column].grid(row=row, column=column)        
        
        self.window.mainloop()
    
    def find_available_squares(self, row, column):
        piece = self.board[row][column]
        
        if piece == "♔" or piece == "♚":   
            for square in self.king_available:
                if square in self.white_pieces.extend(self.black_pieces):
                    available_squares.remove(square)                        

        elif piece == "♕" or piece == "♛":
            return      

        elif piece == "♖" or piece == "♜":
            for i in range(7):
                if (row+i <= 7 and
                    column+i <= 7 and
                    self.board[row+i-1][column] is None):
                    return
        elif piece == "♗" or piece == "♝":
            return

        elif piece == "♘" or piece == "♞":
            for square in self.knight_available:
                if (0 <= row+square[0] <= 7 and 
                    0 <= column+square[1] <= 7):
                    if (self.board[row+square[0]][column+square[1]] not in self.current_player_pieces): 
                        self.available_squares.append([square[0], square[1]])
                        self.squares[row+square[0]][column+square[1]].config(background="#ca5a5a")
                    
        elif piece == "♙" or piece == "♟︎":
            return


    def click(self, row, column):
        if (self.board[row][column] is not None and 
                self.board[row][column] in self.current_player_pieces):
            self.find_available_squares(row, column)
            self.current_piece = [row, column]
            
            for square in self.previous_available_squares:
                self.squares[self.current_piece[0]+square[0]][self.current_piece[1]+square[1]].config(
                    background="#588bb6" if (row+column) % 2 == 0 else "#babcbf"
                )
         
        elif (self.current_piece is not None and
              self.board[row][column] not in self.current_player_pieces):
            self.previous_available_squares = self.available_squares
            self.play(row, column)
            
            for rows in range(8):
                for columns in range(8): 
                    if self.squares[rows][columns] != self.squares[row][column]: 
                        self.squares[rows][columns].config(state="normal")

 
    def play(self, row, column):
        previous_row = self.current_piece[0]
        previous_column = self.current_piece[1]
        
        if [row-previous_row, column-previous_column] in self.available_squares:
            self.board[row][column] = self.board[previous_row][previous_column]
            self.squares[row][column].config(text=self.board[previous_row][previous_column])
        
            self.board[previous_row][previous_column] = None
            self.squares[previous_row][previous_column].config(text="")
            self.current_piece = None
        
            self.pieces.reverse()
            self.current_player_pieces = self.pieces[0]
        
            for square in self.previous_available_squares:
                self.squares[previous_row+square[0]][previous_column+square[1]].config(
                    background="#588bb6" if (row+column) % 2 == 0 else "#babcbf"
                )
            
        else:
            return
        
    def check_checker(self):
        return

Chess()
