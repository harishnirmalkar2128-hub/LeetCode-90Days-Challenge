class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def backtrack(start, cur, remaining):
            if remaining == 0:
                res.append(cur[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i-1]:
                    continue
            
                if candidates[i] > remaining:
                    break

                cur.append(candidates[i])
            
                backtrack(i + 1, cur, remaining - candidates[i])
                cur.pop()

        backtrack(0, [], target)
        return res