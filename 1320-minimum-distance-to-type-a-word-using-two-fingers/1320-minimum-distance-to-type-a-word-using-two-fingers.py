class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_pos(char):
            idx = ord(char) - ord('A')
            return divmod(idx, 6)

        def get_dist(p1, p2):
            if p1 is None or p2 is None: return 0
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        positions = [get_pos(c) for c in word]

        @lru_cache(None)
        def solve(idx, f1_pos, f2_pos):
            if idx == len(word):
                return 0

            target = positions[idx]

            choice1 = get_dist(f1_pos, target) + solve(idx + 1, target, f2_pos)

            choice2 = get_dist(f2_pos, target) + solve(idx + 1, f1_pos, target)
            
            return min(choice1, choice2)

        return solve(0, None, None)