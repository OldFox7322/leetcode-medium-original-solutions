class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = [str(i) for i in s]

        y = []

        g = []

        for i in x:
            if i in y:
                if len(y) > len(g):
                    g = y.copy()
                idx = y.index(i)+1
                del y[:idx]
                y.append(i)
            else:
                y.append(i)
        if len(y) > len(g):
            g = y.copy()

        return len(g)