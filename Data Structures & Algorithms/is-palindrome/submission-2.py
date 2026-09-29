class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""
        for char in s.lower():
            if (ord(char) >= 48 and ord(char) <= 57) or (ord(char) >= 97 and ord(char) <= 122):
                cleaned_s += char
        for i in range(len(cleaned_s)//2):
            if cleaned_s[i] != cleaned_s[len(cleaned_s) - i - 1]:
                return False
        return True