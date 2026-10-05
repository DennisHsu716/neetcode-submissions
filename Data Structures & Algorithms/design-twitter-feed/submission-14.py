class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        self.followmap[userId].add(userId)

        for followee in self.followmap[userId]:
            if self.tweetmap[followee]:
                index = len(self.tweetmap[followee]) - 1
                time, tweetId = self.tweetmap[followee][index]
                heapq.heappush(heap, (-time, tweetId, followee, index))
        
        while heap and len(res) < 10:
            time, tweetId, followee, index = heapq.heappop(heap)
            res.append(tweetId)

            if index > 0:
                index -= 1
                time, tweetId = self.tweetmap[followee][index]
                heapq.heappush(heap, (-time, tweetId, followee, index))
        return res 

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].discard(followeeId)
        
