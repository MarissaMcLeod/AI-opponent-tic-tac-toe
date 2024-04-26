import random
import os

class Player:
    #initialize the player with name and marker
    def __init__(self, name, marker, computer_player=False, difficulty='easy'):
        self.name = name
        self.marker = marker  # Marker is X or O
        self.computer_player = computer_player
        self.difficulty = difficulty  # to select easy or hard difficulty
        
        
def clear_screen():
    #clears console game board and resets after each move
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(board):
    # prints current state of the board
    #clear_screen()
    print("\n----Tic Tac Toe----")
    for row in board.values():
        print("|" + "|".join(row) + "|")
    print("------------------")


def check_win(board):
    # Check rows, columns, and diagonals for a win
    lines = [board[1], board[2], board[3], # Rows
             [board[row][0] for row in board], [board[row][1] for row in board], [board[row][2] for row in board], # Columns
             [board[1][0], board[2][1], board[3][2]], [board[1][2], board[2][1], board[3][0]]] # Diagonals
    return any(line.count(line[0]) == 3 and line[0] != ' ' for line in lines)


def get_computer_move(board, player):
    # decides computer's move based on difficulty level.
    print("Computing move for {0} with difficulty {1}".format(player.name, player.difficulty))
    if player.difficulty == 'easy':
        possible_moves = [(row, col) for row in range(1, 4) for col in range(1, 4) if board[row][col-1] == ' ']
        print("Possible moves for 'easy': {0}".format(possible_moves))
        chosen_move = random.choice(possible_moves)
        return chosen_move
    elif player.difficulty == 'hard':
        move = find_best_move(board, player)
        print("Move chosen by 'hard' algorithm: {0}".format(move))
        return move if move else random.choice([(row, col) for row in range (1, 4) for col in range (1, 4) if board[row][col-1] == ' '])
            
        
def find_best_move(board, player):
    # uses minimax algorithm to determine best move
    best_score = -float('inf')
    best_move = None
    opponent = Player("Opponent", 'X' if player.marker == 'O' else 'O')
    for row in range(1, 4):
        for col in range(1, 4):
            if board[row][col - 1] == ' ':
                board[row][col - 1] = player.marker
                score = minimax(board, False, player, opponent)
                board[row][col - 1] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    if best_move:
        print(f"Best move found: {best_move} with score {best_score}")
        return best_move
    else:
        fallback_move = random.choice([(row, col) for row in range(1, 4) for col in range(1, 4) if board[row][col-1] == ' '])
        print(f"No optimal move determined, selecting random fallback move: {fallback_move}")
        return fallback_move
    

#implement minimax algorithm for hard difficulty 
def minimax(board, is_maximizing, player, opponent):
    # check terminal conditions
    if check_win(board):
        if is_maximizing:
            return -10 # computer loss
        else:
            return 10 # computer win
    if all(cell != ' ' for row in board.values() for cell in row):
        return 0  #draw

    if is_maximizing:
        best_score = -float('inf')
        for row in range(1, 4):
            for col in range(1, 4):
                if board[row][col - 1] == ' ':
                    board[row][col - 1] = player.marker
                    score = minimax(board, False, player, opponent)
                    board[row][col - 1] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(1, 4):
            for col in range(1, 4):
                if board[row][col - 1] == ' ':
                    board[row][col - 1] = opponent.marker
                    score = minimax(board, True, player, opponent)
                    board[row][col - 1] = ' '
                    best_score = min(best_score, score)
        return best_score


def game():
    game_board = {1: [' ', ' ', ' '], 2: [' ', ' ', ' '], 3: [' ', ' ', ' ']}

    # Setup players
    player1_name = input("Please enter Player 1's name: ")
    player2_type = input("Will Player 2 be a person (P) or a computer (C)? [P/C]: ").upper()
    if player2_type == "C":
        while True:
            difficulty = input("Choose difficulty level (easy/hard): ").lower()
            if difficulty in ['easy', 'hard']:
                break
            else:
                print("Invalid difficulty level entered. Please type 'easy' or 'hard'.")
        player2 = Player("Computer", 'O', computer_player=True, difficulty=difficulty)
    else:
        player2 = Player(input("Please enter Player 2's name: "), 'O')

    turn = player1 = Player(player1_name, 'X')

    for _ in range(9):
        
        if turn.computer_player:
            print("Computer is thinking...")
            row, col = get_computer_move(game_board, turn)
            col -= 1
            game_board[row][col] = turn.marker
            print(turn.name + "'s move was (" + str(row) + ", " + str(col + 1) + ")")
            
        else:
            print_board(game_board)  #clears screen and display before player 1's turn
            while True:
                try:
                    user_input = input("{0}'s turn ({1}). Enter row col: ".format(turn.name, turn.marker))
                    row, col = map(int, user_input.split())
                    if game_board[row][col-1] == ' ':
                        game_board[row][col-1] = turn.marker
                        break
                    else:
                        print("That space is taken. Please choose another.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter row and column as two numbers from 1 to 3, separated by a space.")      

        if check_win(game_board):
            print("{0} wins!".format(turn.name))
            return

        turn = player2 if turn == player1 else player1

    print("It's a tie!")


if __name__ == "__main__":
    game()

