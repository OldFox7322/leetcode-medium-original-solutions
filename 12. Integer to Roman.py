class Solution:
    def intToRoman(self, num: int) -> str:
        s = {'M': 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        y = [int(i) for i in str(num)]
        roman = []
        if len(y) > 3:
            a = y[-4]
            a *= 1000
            while a > 0:
                for key, value in s.items():
                    if value <= a:
                        roman.append(key)
                        a -= value
                        break
        if len(y) > 2:
            if y[-3] == 4:
                roman.append('CD')
            elif y[-3] == 9:
                roman.append('CM')
            else:
                a = y[-3]
                a *= 100
                while a > 0:
                    for key, value in s.items():
                        if value <= a:
                            roman.append(key)
                            a -= value
                            break
        if len(y) > 1:
            if y[-2] == 4:
                roman.append('XL')
            elif y[-2] == 9:
                roman.append('XC')
            else:
                a = y[-2]
                a *= 10
                while a > 0:
                    for key, value in s.items():
                        if value <= a:
                            roman.append(key)
                            a -= value
                            break
        if len(y) > 0:
            if y[-1] == 4:
                roman.append('IV')
            elif y[-1] == 9:
                roman.append('IX')
            else:
                a = y[-1]
                while a > 0:
                    for key, value in s.items():
                        if value <= a:
                            roman.append(key)
                            a -= value
                            break
        if roman:
            result = str(''.join(map(str, roman)))
            return result
        return 0
        