#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened
"""


from collections import deque


def canUnlockAll(boxes):
    """
    Checking all visited boxes
    """
    if not boxes or not boxes[0]:
        return False  # No boxes or the first box is empty

    n = len(boxes)
    visited = [False] * n  # To keep track of visited boxes
    visited[0] = True  # Mark the first box as visited
    queue = deque([0])  # Start with the first box

    while queue:
        current_box = queue.popleft()

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
