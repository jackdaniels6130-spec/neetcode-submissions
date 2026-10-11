class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str_to_num(str_num):
            num_dict = {
                '1':1,
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9,
                '0':0
            }

            power = len(str_num) - 1
            ans_num = 0
            for digit in str_num:
                ans_num += num_dict[digit] * (10 ** power)
                power -= 1
                
            return ans_num
        return str(str_to_num(num1) * str_to_num(num2))