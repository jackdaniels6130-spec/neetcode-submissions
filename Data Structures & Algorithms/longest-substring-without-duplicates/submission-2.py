class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        queue = []
        for i in range(len(s)):
            if s[i] in queue:
                idx = queue.index(s[i])
                queue = queue[idx+1:]
            queue.append(s[i])
            longest = max(longest, len(queue))
        return longest