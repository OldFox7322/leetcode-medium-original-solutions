class Solution:
    def longestPalindrome(self, s: str) -> str:
        x = [str(i) for i in s]


        a = 0
        b = 0
        result = []

        for i in range(len(x)):
            for j in range(i+1, len(x)):
                if x[i] == x[j] and j - i <= 2:
                    left = i
                    right = j
                    while left >= 0 and right in range(len(x)):
                        if x[right] == x[left]:
                            if right - left > b - a:
                                a = left
                                b = right
                            left -= 1
                            right += 1
                        else:
                            break

        for i in range(a, b+1):
            result.append(x[i])
            
        result_word = str(''.join(map(str, result)))

        return result_word


        