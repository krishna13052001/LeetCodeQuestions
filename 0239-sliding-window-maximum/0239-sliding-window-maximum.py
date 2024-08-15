class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        res = []
        for i in range(len(nums)):
            if len(queue) >0 and queue[0] <= i - k:
                queue.popleft()
            while len(queue) >0 and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k -1:
                res.append(nums[queue[0]])
        return res
                