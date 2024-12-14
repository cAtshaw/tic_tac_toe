#I'll need to make some sort of table or grid to place the tacs onto
board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
]

#Making a function to display output of the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----") 


#Player will have to use an input for what row or column they want to play into
def player_input(board, player):
    while True:
        try:
            row = int(input(f"{player}, enter row (1-3): ")) - 1 
            col = int(input(f"{player}, enter column (1-3): ")) - 1
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again")
        except ValueError:
            print("Invalid input. Please enter numbers.")

#We'll need to update the board with the players move
def make_move(board, row, col, player):
    board[row][col] = player


#Checking for a win
def check_win(board, player):
    #Checking rows
    for row in board:
        if all(cell == player for cell in row):
            return True
        
    #Checking columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
        
    #Checking for diagonal
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False


#There could be potential for a draw so we'll need to write a draw function
def check_draw(board):
    for row in board:
        if " " in row:
            return False
        return True
    

#Running the main games loop we need to create a main game function



def play_tic_tac_toe():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
]
    
current_player = "X"

while True:
    print_board(board)
    row, col = player_input(board, current_player)
    make_move(board, row, col, current_player)

    if check_win(board, current_player):
        print_board(board)
        print(f"{current_player} wins!")
        break
    elif check_draw(board):
        print_board(board)
        print("Its a draw!")
        break

    current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":

    play_tic_tac_toe()


