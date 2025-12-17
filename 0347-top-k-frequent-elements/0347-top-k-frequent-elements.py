import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        print(count)
        heap = []

        for nums, f in count.items():
            heapq.heappush(heap, (f, nums))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for f, num in heap]