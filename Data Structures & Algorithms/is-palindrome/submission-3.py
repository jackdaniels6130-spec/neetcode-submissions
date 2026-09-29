class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""
        for char in s.lower():
            if char.isalnum():
                cleaned_s += char
        return cleaned_s == cleaned_s[::-1]