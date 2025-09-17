"""
For this problem the goal is to substitute at most k chars in the string to 
get the longest substring with the same char.

We use the sliding window approach because we are looking for a contiguous substring.

This time, the tricky part is to keep track of the character with the highest frequency in the current window.
When found, we can calculate how many chars need to be replaced to make all chars in the window the same.
Ff the number of chars to be replaced exceeds k, we need to shrink the window from the left.

There are two ways to keep track of the character with the highest frequency:

1. Recalculate the max frequency in the current window every time we expand or shrink the window.
   This can be done using max(count.values()), but it is inefficient and can lead to O(n^2) time complexity in the worst case.
   Worst case happens when we have to shrink the window often, and each time we shrink, we recalculate the max frequency.

2. Maintain a variable maxf that keeps track of the highest frequency seen so far in the window.
   This variable is updated whenever we expand the window to the right.

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0 # keep track of the character with the highest frequency
        for r in range(len(s)): # loop actually ends when right pointer can no longer go to the right
            count[s[r]] = 1 + count.get(s[r], 0) # if doesn't exist, 0
            maxf = max(maxf, count[s[r]])

            while (r - l + 1 - maxf) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res

# Recalculating max frequency every time (inefficient):
count = {}

max(count.values())

# Maintaining maxf variable (efficient):
maxf = 0
maxf = max(maxf, count[s[r]]) # where s[r] is the newly added character to the window)

