#!/usr/bin/python3
"""
tic.py - Tic Tac Toe game with bug fixes
Fixed: winner detection, tie detection, input validation
"""

def print_board(board):
    """Print the Tic Tac Toe board"""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:  # Don't print after last row
            print("-" * 9)

def check_winner(board, player):
    """
    Check if a player has won the game.
    
    Args:
        board (list): 3x3 game board
        player (str): "X" or "O"
    
    Returns:
        bool: True if player has won
    """
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    """Check if the board is full (tie condition)"""
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(prompt):
    """
    Get valid integer input from user (0, 1, or 2)
    
    Args:
        prompt (str): Input prompt
    
    Returns:
        int: Valid integer between 0-2
    """
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 2:
                return value
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    """Main game function"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    moves = 0
    
    print("Welcome to Tic Tac Toe!")
    print("Player X goes first, then Player O.")
    print("Enter row and column numbers (0, 1, or 2).")
    
    while True:
        print(f"\nCurrent board:")
        print_board(board)
        
        # Get player move
        print(f"\nPlayer {player}'s turn")
        row = get_valid_input("Enter row (0, 1, or 2): ")
        col = get_valid_input("Enter column (0, 1, or 2): ")
        
        # Check if spot is available
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue
        
        # Make the move
        board[row][col] = player
        moves += 1
        
        # Check for win
        if check_winner(board, player):
            print_board(board)
            print(f"\n🎉 Congratulations! Player {player} wins! 🎉")
            break
        
        # Check for tie
        if moves == 9:
            print_board(board)
            print("\n🤝 It's a tie! 🤝")
            break
        
        # Switch player
        player = "O" if player == "X" else "X"
    
    print("\nThanks for playing!")

if __name__ == "__main__":
    tic_tac_toe()
