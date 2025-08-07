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

# Time Complexity:  O(N*log(N)) -> getNewsFeed(), number of followers of a given user id
# Space Complexity: O(N+M) -> the Twitter class in general |
# N -> number of tweets, M -> number of follow relationships
## Time and Space complexity for all other functions is ""O(1)""
import collections
import heapq


class Twitter:

    def __init__(self):
        self.tweet_map = collections.defaultdict(
            list
        )  # {userId: [time_stamp, tweet_id]}
        self.follow_map = collections.defaultdict(
            set
        )  # {follower_id: set(followee_id)}
        self.time_stamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.time_stamp, tweetId])
        self.time_stamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        followees = self.follow_map[userId]
        followees.add(userId)

        max_heap = []
        for followee in followees:
            for time_stamp, tweet_id in self.tweet_map[followee]:
                heapq.heappush(max_heap, [-time_stamp, tweet_id])

        result = []
        while max_heap and len(result) < 10:
            result.append(heapq.heappop(max_heap)[1])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)


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
    "unfollow": Twitter.unfollow,
}

err_msg_invalid_result = (
    "Provided result is not correct for the given function. Something is wrong!"
)

# Test Case - 1
ops_one = [
    "Twitter",
    "postTweet",
    "getNewsFeed",
    "follow",
    "postTweet",
    "getNewsFeed",
    "unfollow",
    "getNewsFeed",
]
vals_one = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
expected_results = [None, None, [5], None, None, [6, 5], None, [5]]

for op, val, expected_result in zip(ops_one, vals_one, expected_results):
    if op == "Twitter":
        twitter = Twitter()
        # Update the "twitter" instance
        ops_dict[op] = twitter
        continue

    if op == "getNewsFeed":
        result = ops_dict[op](twitter, val[0])
    else:
        result = ops_dict[op](twitter, val[0], val[1])

    assert result == expected_result, err_msg_invalid_result
    print(result)
