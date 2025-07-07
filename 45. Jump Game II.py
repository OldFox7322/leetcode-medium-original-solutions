class Solution:
    def jump(self, nums: List[int]) -> int:

        steps = 0

        result = 0

        max_index = 0

        result = 0

        max_iteration = 0


        if len(nums) == 1:
            return 0


        while result < len(nums) - 1:
            steps += 1
            for index, value in enumerate(nums):
                if index > max_index:
                    break
                else:
                    iteration = index + value
                    if iteration > max_iteration:
                        max_iteration = iteration
            max_index = max_iteration
            result = max_iteration

        return steps

        