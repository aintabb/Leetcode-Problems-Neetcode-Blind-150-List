"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:
Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.


Example 1:
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.


Constraints:
1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 104
All the tweets have unique IDs.
At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
"""

import heapq
from collections import defaultdict

# Time Complexity:  O(N) -> getNewsFeed(), number of followers of a given user id
# Space Complexity: O(N) -> getNewsFeed()
## Time and Space complexity for all other functions is ""O(1)""
class Twitter:

    def __init__(self) -> None:
        self.time_stamp = 0
        self.tweet_map = defaultdict(list) # pair of [time_stamp, tweet_id]
        self.follow_map = defaultdict(set) # [follower_id, followee_id]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.time_stamp, tweetId])
        self.time_stamp -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        result, min_heap = [], []

        # Users should be able to see their posts
        self.follow_map[userId].add(userId)

        for followee_id in self.follow_map[userId]:
            # If the followee has any tweets
            if followee_id in self.tweet_map:
                # Get the most recent tweet's index
                index_of_last = len(self.tweet_map[followee_id]) - 1
                time_stamp, tweet_id = self.tweet_map[followee_id][index_of_last]

                min_heap.append([time_stamp, tweet_id, followee_id, index_of_last - 1])

        heapq.heapify(min_heap)

        while min_heap and len(result) < 10:
            time_stamp, tweet_id, followee_id, index_of_last = heapq.heappop(min_heap)
            result.append(tweet_id)

            if (index_of_last >= 0):
                time_stamp, tweet_id = self.tweet_map[followee_id][index_of_last]
                heapq.heappush(min_heap, [time_stamp, tweet_id, followee_id, index_of_last - 1])

        return result


    def follow(self, followerId: int, followeeId: int) -> None:
       self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

ops_dict = {
  "Twitter": Twitter,
  "postTweet": Twitter.postTweet,
  "getNewsFeed": Twitter.getNewsFeed,
  "follow": Twitter.follow,
  "unfollow": Twitter.unfollow
}

err_msg_invalid_result = "Provided result is not correct for the given function. Something is wrong!"

test_cases  = []

# Test Case - 1
ops_one   = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
vals_one  = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
expected_results = [None, None, [5], None, None, [6, 5], None, [5]]

for op, val, expected_result in zip(ops_one, vals_one, expected_results):
    if op == "Twitter":
        twitter = Twitter()
        # Update the "twitter" instance
        ops_dict[op] = twitter
        continue

    if (op == "getNewsFeed"):
        result = ops_dict[op](twitter, val[0])
    else:
        result = ops_dict[op](twitter, val[0], val[1])

    assert result == expected_result, err_msg_invalid_result
    print(result)