from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort()
        
        n = len(robot)
        m = len(factory)
        
        @lru_cache(None)
        def solve(robot_idx, factory_idx):
            if robot_idx == n:
                return 0
            if factory_idx == m:
                return float('inf')
            
            res = solve(robot_idx, factory_idx + 1)
            
            total_dist = 0
            for k in range(factory[factory_idx][1]):
                if robot_idx + k >= n:
                    break
                
                total_dist += abs(robot[robot_idx + k] - factory[factory_idx][0])
                next_res = solve(robot_idx + k + 1, factory_idx + 1)
                
                if next_res != float('inf'):
                    res = min(res, total_dist + next_res)
                    
            return res
            
        return solve(0, 0)