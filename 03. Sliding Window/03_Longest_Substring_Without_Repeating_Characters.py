class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # o(n) sliding window
        res = 0
        charSet = set()

        l = 0

        for r in range(len(s)):
            while s[r] in charSet: # if char is already in the set, move the left pointer / shrink the window
                charSet.remove(s[l]) # remove leftmost char BEFORE updating the left pointer
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res 
    
"""
For this problem, we use the sliding window technique to find the length of the longest substring without repeating characters.

The idea is to maintain a window using two pointers (left and right) that represents the current substring being examined. 

We use a set to keep track of the characters in the current window.

Operations to remember: .remove(), add() for sets.

"""