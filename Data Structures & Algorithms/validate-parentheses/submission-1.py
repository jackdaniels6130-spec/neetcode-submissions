class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
                ')' : '(',
                ']' : '[',
                '}' : '{'
        }

        for p in s:
            if p in pairs:
                if not stack or stack[-1] != pairs[p]:
                    return False
                stack.pop()
            else:
                stack.append(p)
        if not stack:
            return True
        return False

                