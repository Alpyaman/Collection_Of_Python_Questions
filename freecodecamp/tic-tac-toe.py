"""
Given a NxN matrix (an array of arrays) representing a completed Tic-Tac-Toe game, determine the winner.

Each element in the given matrix is either an "X" or "O".
A player wins if they have three of their characters in a row - horizontally, vertically, or diagonally.

Return:

"X wins" if player X has three in a row.
"O wins" if player O has three in a row.
"Draw" if no player has three in a row.
"""

def check_n_by_n_tic_tac_toe(board: list[list[str]]) -> str:
    """
    Determines the winner of a Tic-Tac-Toe game.

    Args:
        board (list of list of str): A NxN matrix representing the Tic-Tac-Toe board.
    
    Returns:
        str: "X wins", "O wins", or "Draw" based on the game result.
    """
    N = len(board)

    # 1. Check Rows
    for row in board:
        if all(cell == row[0] for cell in row):
            return f"{row[0]} wins"
    
    # 2. Check Columns
    for col in range(N):
        if all(board[row][col] == board[0][col] for row in range(N)):
            return f"{board[0][col]} wins"
    
    # 3. Check Diagonals
    if all(board[i][i] == board[0][0] for i in range(N)):
        return f"{board[0][0]} wins"
    
    if all(board[i][N-1-i] == board[0][N-1] for i in range(N)):
        return f"{board[0][N-1]} wins"
    
    return "Draw"

# --- Example Usage ---

# Example 1: 4x4 Board (O wins on anti-diagonal)
game_4x4 = [
    ["X", "X", "X", "O"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
    ["O", "X", "X", "X"]
]

# Example 2: 2x2 Board (X wins vertically)
game_2x2 = [
    ["X", "O"],
    ["X", "O"]
]

print(f"4x4 Result: {check_n_by_n_tic_tac_toe(game_4x4)}") # Output: O wins
print(f"2x2 Result: {check_n_by_n_tic_tac_toe(game_2x2)}") # Output: X wins