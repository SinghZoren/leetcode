# Though Process:
# 1. Sort the string to help with skipping duplicates.
# 2. Use backtracking to generate all distinct permutations of the string.
# 3. Store each valid permutation in a set to avoid duplicates.
# 4. For each permutation store it in the vairuble 'currentPermutation'.
# 5. Iterate through each charater in ''currentPermutation':
#    - Add digits at even indices to even_sum.
#    - Add digits at odd indices to odd_sum.
# 6. If even_sum == odd_sum, increment the count.
# 7. Return the count modulo 10^9 + 7.

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        results = set()

        def backtrack(path: list[str], used: list[bool]):
            if len(path) == len(num):
                results.add(''.join(path))
                return
            for i in range(len(num)):
                if used[i]:
                    continue
                if i > 0 and num[i] == num[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(num[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

        num = ''.join(sorted(num))
        backtrack([], [False] * len(num))

        count = 0
        for perm in results:
            currentPermutation = perm
            even_sum = 0
            odd_sum = 0
            for i, digit in enumerate(currentPermutation):
                if i % 2 == 0:
                    even_sum += int(digit)
                else:
                    odd_sum += int(digit)
            if even_sum == odd_sum:
                count += 1
        return count % MOD