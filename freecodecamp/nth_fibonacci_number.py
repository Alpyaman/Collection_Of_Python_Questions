"""
Given an integer n, return the nth number in the fibonacci sequence.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
"""
def nth_fibonacci_number(n: int) -> int:
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    
    a, b = 0, 1
    
    for _ in range(n):
        a, b = b, a + b
    
    return a

# --- Example Usage ---
print(f"F(0): {nth_fibonacci_number(0)}")   # Output: 0
print(f"F(1): {nth_fibonacci_number(1)}")   # Output: 1
print(f"F(10): {nth_fibonacci_number(10)}") # Output: 55

# --- Additional Implementation: Top-Down Dynamic Programming (Memoization) ---
def fib_memo(n: int, memo = {}) -> int:
    """
    Calculates Fibonacci(n) using Top-Down Dynamic Programming (Memoization).
    """
    # 1. Check if we already know the answer
    if n in memo:
        return memo[n]
    
    # 2. Base case
    if n <= 1:
        return n
    
    # 3. Calculate and store (memoize) the answer
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]

# Usage
# The 'memo' dict persist across calls if defined outside or passed explicitly
print(fib_memo(10))  # Output: 55
print(fib_memo(50))  # Output: 12586269025 Returns quickly due to memoization

# --- Additional Implementation: Bottom-Up Dynamic Programming (Tabulation) ---
def fib_tabulation(n: int) -> int:
    """
    Calculates Fibonacci(n) using Bottom-Up Dynamic Programming (Tabulation).
    """
    if n <= 1:
        return n
    
    # 1. Create a table to store Fibonacci values
    table = [0] * (n + 1)
    
    # 2. Base cases
    table[0] = 0
    table[1] = 1
    
    # 3. Fill the table iteratively
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    
    return table[n]

# Usage
print(fib_tabulation(10))  # Output: 55
print(fib_tabulation(50))  # Output: 12586269025 Returns quickly due to tabulation