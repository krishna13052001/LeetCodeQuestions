class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        total_dist = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            ghost_dist = abs(target[0]-ghost[0]) + abs(target[1]-ghost[1])
            print(total_dist,ghost_dist)
            if(ghost_dist<=total_dist):
                return False
        return True