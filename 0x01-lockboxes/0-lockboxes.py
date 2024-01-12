#!/usr/bin/python3
"""Solution to Lockboxes problem"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes: List of lists representing the boxes and keys.

    Returns:
    - True if all boxes can be opened, else False.
    """
    # Set to keep track of opened boxes
    opened_boxes = set()
    opened_boxes.add(0)  # The first box is unlocked initially

    # List to keep track of new keys discovered during each iteration
    new_keys = [0]

    # Continue until there are no more new keys
    while new_keys:
        current_key = new_keys.pop()

        # Iterate through the keys in the current box
        for key in boxes[current_key]:
            # If the key opens a new box and that box is not already opened
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                new_keys.append(key)

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)
