class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sq_sum(n):
            sum = 0
            while n > 0:
                digit = n % 10
                sum += digit ** 2
                n = n // 10
            return sum

        seen = set()
        sum = get_sq_sum(n)
        print(sum)
        while True:
            sum = get_sq_sum(sum)
            print(sum)
            if sum == 1:
                return True
            if sum in seen:
                return False
            seen.add(sum)
        return False

    