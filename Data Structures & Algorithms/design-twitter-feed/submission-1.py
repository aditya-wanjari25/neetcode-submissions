import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        # Time counter to keep tweets chronological. 
        # We decrement it so smaller negative numbers = more recent (Max-Heap simulation)
        self.time = 0
        
        # Maps userId -> list of (time, tweetId)
        self.tweet_map = defaultdict(list)
        
        # Maps userId -> set of followeeIds. Sets make follow/unfollow O(1) and prevent duplicates.
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append the tweet to the user's personal list with the current timestamp
        self.tweet_map[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        min_heap = []
        
        # A user always sees their own tweets in their feed
        self.follow_map[userId].add(userId)
        
        # 1. Initialize the heap with the single most recent tweet from each person they follow
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                # Get the index of their most recent tweet (the last one in their list)
                index = len(self.tweet_map[followeeId]) - 1
                tweet_time, tweetId = self.tweet_map[followeeId][index]
                
                # Push the tweet into the heap, along with the followeeId and the next index to check
                heapq.heappush(min_heap, (tweet_time, tweetId, followeeId, index - 1))
        
        # 2. Pop the 10 most recent tweets overall
        while min_heap and len(res) < 10:
            tweet_time, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            
            # If the person whose tweet we just popped has more older tweets, 
            # push their next most recent tweet into the heap
            if index >= 0:
                next_time, next_tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(min_heap, (next_time, next_tweetId, followeeId, index - 1))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Safely remove without throwing an error if it doesn't exist
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)