# Thought process
# 1. Create a dictionary to store the numbers and their indices.
# 2. Iterate through the list of numbers.
# 3. For each number, calculate its complement (target - number).
# 4. Check if the complement is already in the dictionary.
# 5. If it is, return the indices of the current number and its complement.
# 6. If not, add the current number and its index to the dictionary.
# 7. If no solution is found, return an empty list.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        return []