class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = [0] * 26
        for char in s1:
            freq_s1[ord(char) - ord('a')] += 1

        window_size = len(s1)
        for i in range(len(s2) - window_size+1):
            freq_s2 = [0] * 26
            for char in s2[i: window_size + i]:
                freq_s2[ord(char) - ord('a')] += 1
            if freq_s2 == freq_s1:
                return True
        return False