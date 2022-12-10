# longest substring without repeating characters

""" 
Given a string s, find the length of the longest 
substring
 without repeating characters.

 Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
 """
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start = 0
        end = 0
        max_len = 0
        visited = set()
        while end < len(s):
            if s[end] not in visited:
                visited.add(s[end])
                # max will be the length of the set visited
                max_len = max(max_len, len(visited))
                end += 1
            else:
                # we remove because we have seen the character
                visited.remove(s[start])
                start += 1
        return max_len