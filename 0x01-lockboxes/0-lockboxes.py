#!/usr/bin/python3
"""
This Module is for making the lockboxes in the most optimal way
"""

def canUnlockAll(boxes):
    """
    Args:
        - boxes: list of boxes to iterate over
    Return:
        - False: when we can't access all the boxes
        - True: when we can access all the boxes throught the list
    """
    seen = set([0])
    stack = [0]
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < len(boxes) and key not in seen:
                stack.append(key)
                seen.add(key)
    return len(seen) == len(boxes)
