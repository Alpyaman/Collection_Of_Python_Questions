"""
# Left-Handed Seat at the Table
Given a 2xN matrix (array of arrays) representing the seating arrangement for a meal,
determine how many seats a left-handed person can sit at.

A left-handed person cannot sit where a right-handed person would be in the seat to the immediate left of them.
In the given matrix:

An "R" is a seat occupied by a right-handed person.
An "L" is a seat occupied by a left-handed person.
An "U" is an unoccupied seat.

Only unoccupied seats are available to sit at.
The seats in the top row are facing "down", and the seats in the bottom row are facing "up" (like a table),
so left and right are relative to the seat's orientation.

Corner seats only have one seat next to them.
For example, in the given matrix:

[
  ["U", "R", "U", "L"],
  ["U", "R", "R", "R"]
]

The top-left seat is cannot be sat in because there's a right-handed person to the left.
The other two open seats can be sat in because there isn't a right-handed person to the left.
"""

def count_left_handed_seats(table: list[list[str]]) -> int:
    """
    Counts available seats for a left-handed person given a 2xN seating arrangement.

    Args:
        table (list of list of str): A 2xN matrix representing the seating arrangement.
    
    Returns:
        int: The number of seats available for a left-handed person.
    """
    count = 0
    rows = len(table)
    cols = len(table[0]) if rows > 0 else 0

    # 1. Check Top Row (Index 0) - Facing Down
    # "Left" is towards higher index (col + 1)
    for col in range(cols):
        seat = table[0][col]

        if seat == "U":
            # Check the neighbor to the immediate left (col + 1)
            # If we are at the last column, there's no neighbor to the left
            if col + 1 < cols:
                neighbor = table[0][col + 1]
                if neighbor == "R":
                    continue # Blocked by right-handed person
            count += 1
        
    # 2. Check Bottom Row (Index 1) - Facing Up
    # "Left" is towards lower index (col - 1)
    for col in range(cols):
        seat = table[1][col]

        if seat == "U":
            # Check the neighbor to the immediate left (col - 1)
            # If we are at the first column, there's no neighbor to the left
            if col - 1 >= 0:
                neighbor = table[1][col - 1]
                if neighbor == "R":
                    continue # Blocked by right-handed person
            count += 1
    
    return count 

# Example usage:
seating_chart = [
  ["U", "R", "U", "L"],
  ["U", "R", "R", "R"]
]

result = count_left_handed_seats(seating_chart)
print(f"Valid seats for left-handed person: {result}") 
# Output: 2