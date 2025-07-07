class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s1 = [str(i) for i in str(s)]
        y = []
        step_max = numRows*2 - 2
        if len(s) < 2 or numRows < 2:
            return s


  
        for i in range(1, numRows+1):
            y.append(i)
            step = numRows*2 - i*2
            result = step + i
            if result < len(s1)+1:
                y.append(result)
                while True:
                    new_step = step_max - step
                    step = new_step
                    result += new_step 
                    if result > len(s1):
                        break
                    if result <= len(s1):
                        y.append(result)

        response = []


        result_nums = list(dict.fromkeys(y))
        for i in result_nums:
            i -= 1
            if i in range(len(s)):
                response.append(s1[i])

        result_word = str(''.join(map(str, response)))

        return result_word
        