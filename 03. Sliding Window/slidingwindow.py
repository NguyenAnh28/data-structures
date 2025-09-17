"""
The sliding window technique

When to use:
- When the problem involves finding a substring or subarray that satisfies certain conditions.

How to use:
- Use two pointers to represent the current window (left and right).
- Expand the right pointer to include more elements in the window.
- Shrink the left pointer to exclude elements from the window when the conditions are not met.
"""

l = 0

for r in range(len(s)): # loop ends when right pointer can no longer go to the right
    # expand the window by moving the right pointer
    # update data structures to include s[r]
    while not condition_met:
        l += 1
    res = max(res, r - l + 1)