class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if either of s or t is null, there would be no min sutstring, return empty string
        if not s or not t:
            return ""

        # count the freq of every char in t, so that we can later use it
        # to check if our substring has all the required char or not (with their correct freq)
        freq_t = {}
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1
        # print(freq_t)

        # 2 pointers for to 
        left = 0
        right = 0
        # have and need to understand if our substring have all the 
        # required chars from t
        have = 0
        need  = len(freq_t)

        min_len = float('inf')
        min_start = 0
        window_freq = {}

        for right in range(len(s)):
            char = s[right]

            if char in freq_t:
                window_freq[char] = window_freq.get(char, 0) + 1

                if window_freq[char] == freq_t[char]:
                    have += 1

            # enter the while loop only when we have the required 
            # chars in our substring, and keep on shrinking from left
            # and remember the min_start, and min_len
            while have == need:
                # current window is valid
                window_len = right - left + 1

                if window_len < min_len:
                    min_len = window_len
                    min_start = left

                # remove left character
                left_char = s[left]

                if left_char in freq_t:
                    if window_freq[left_char] == freq_t[left_char]:
                        have -= 1

                    window_freq[left_char] -= 1
                left += 1
        if min_len == float('inf'):
            return ""
        return s[min_start: min_start + min_len]