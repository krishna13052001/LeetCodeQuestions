from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followed = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        followed = self.followed[userId] | {userId}

        for u in followed:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                t, tid = self.tweets[u][idx]
                heapq.heappush(heap, (-t, tid, u, idx))

        result = []
        while heap and len(result) < 10:
            neg_t, tid, u, idx = heapq.heappop(heap)
            result.append(tid)

            if idx - 1 >= 0:
                t2, tid2 = self.tweets[u][idx - 1]
                heapq.heappush(heap, (-t2, tid2, u, idx - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followed[followerId].discard(followeeId)
