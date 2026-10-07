class Solution:

    def encode(self, strs: List[str]) -> str:
        en_str = ""
        for word in strs:
            en_str += (f'{len(word)}#{word}')
        return en_str
    def decode(self, s: str) -> List[str]:
        i = 0
        decode_list = []
        while i < len(s):
            num = ""
            word_len = 0
            while s[i].isnumeric():
                num += s[i]
                i += 1
            word_len += len(num) + 1
            decode_list.append(s[i+1: i+int(num) + 1])
            word_len += len(s[i+1: i+ int(num) + 1])
            i += word_len - len(num)
        return decode_list