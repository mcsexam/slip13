def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
    for i in range(3):
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)] 
    player = "X" 
    win = False 
    print("Tic-Tac-Toe Game:")
    print_board(board)

    while not win and not check_draw(board):
        print(f"Player {player}, enter your move (row and column):")
        try:
            row, col = map(int, input().split())
        except ValueError:
            print("Invalid input. Enter two numbers separated by a space (e.g., 1 2).")
            continue

        if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == " ":
            board[row - 1][col - 1] = player  
            print_board(board) 

            win = check_win(board, player)

            if not win:
                player = "O" if player == "X" else "X"
        else:
            print("Invalid move! Position must be 1–3 and must be empty.")
    
    if win:
        print(f"Player {player} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
