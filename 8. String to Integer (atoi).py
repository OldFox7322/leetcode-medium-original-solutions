class Solution:
    def myAtoi(self, s: str) -> int:
        s1 = [str(i) for i in str(s)]
        m = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '+', ' ']
        y = []
        p = []
        for i in s1:
            if i in "+- " and y:
                break
            elif i in "+- " and p:
                break
            elif not y and i in '0+':
                p.append(i)
            elif i not in m:
                break
            elif i in m:
                y.append(i)
        if y and y[-1] != '-':
            result = int(''.join(map(str, y)))
            if result > 2147483647:
                return(2147483647)
            if result < -2147483648:
                return(-2147483648)
            return(result)
        else:
            return(0)
            

        
        