class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        minus = 0
        if dividend < 0:
            minus += 1
        if divisor < 0:
            minus += 1
        x = abs(dividend) 
        y = abs(divisor)
        lenx = [str(i) for i in str(dividend)]
        if y == 1:
                result = x 
                y = 0
                x = 0
        elif len(lenx) > 8 and y < 10:
            y = y + y + y + y + y + y + y + y + y + y
            y = y + y + y + y + y + y + y + y + y + y
            while x >= y:
                x -= y
                result += 100
        y = abs(divisor)

        while x >= y:
            x -= y
            result += 1
        if minus == 1:
            result = -result
        if result < -2147483648:
            result = -2147483648

        if result > 2147483647:
            result = 2147483647

        return result