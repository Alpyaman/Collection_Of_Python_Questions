def hanoi_solver(n):
    """
    Solves the Tower of Hanoi puzzle and returns the state of the rods at each step.

    Args:
        n (int): The total number of disks.

    Returns:
        str: A string representing the state of the rods at each step, 
             separated by newlines.
    """
    # Initialize the rods. 
    # Rod 0 starts with disks n down to 1. Rods 1 and 2 are empty.
    # We use lists of integers to represent the rods.
    rods = [list(range(n, 0, -1)), [], []]
    
    # This list will store the formatted string for each step
    history = []

    def capture_state():
        """Helper to format the current state of rods into a string."""
        # Using f-strings with the lists directly produces the required format:
        # e.g., "[3, 2, 1] [] []"
        history.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def move(k, source_idx, target_idx, aux_idx):
        """
        Recursive function to move k disks from source to target.
        
        Args:
            k: Number of disks to move
            source_idx: Index of the source rod (0, 1, or 2)
            target_idx: Index of the target rod
            aux_idx: Index of the auxiliary rod
        """
        if k == 0:
            return

        # Step 1: Move k-1 disks from source to auxiliary
        move(k - 1, source_idx, aux_idx, target_idx)

        # Step 2: Move the kth disk (the largest of this batch) from source to target
        disk = rods[source_idx].pop()
        rods[target_idx].append(disk)
        
        # Record the state after the physical move
        capture_state()

        # Step 3: Move the k-1 disks from auxiliary to target
        move(k - 1, aux_idx, target_idx, source_idx)

    # --- Execution Start ---
    
    # 1. Capture the initial starting state
    capture_state()
    
    # 2. Start the recursive solver
    # Move n disks from Rod 0 to Rod 2, using Rod 1 as auxiliary
    move(n, 0, 2, 1)

    # 3. Join all history states with a newline and return
    return "\n".join(history)
