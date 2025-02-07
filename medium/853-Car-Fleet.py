"""
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.


Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3

Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Example 2:
Input: target = 10, position = [3], speed = [3]
Output: 1

Explanation: There is only one car, hence there is only one fleet.

Example 3:
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1

Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.


Constraints:
n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 106
"""

# Time Complexity:  O(N*LogN)
# Space Complexity: O(N)


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]

        result = self.car_fleet(target, position, speed)
        assert result == 3, err_msg_invalid_result
        print(result)

        target = 10
        position = [3]
        speed = [3]

        result = self.car_fleet(target, position, speed)
        assert result == 1, err_msg_invalid_result
        print(result)

        target = 100
        position = [0, 2, 4]
        speed = [4, 2, 1]

        result = self.car_fleet(target, position, speed)
        assert result == 1, err_msg_invalid_result
        print(result)

    def car_fleet(self, target: int, position: list[int], speed: list[int]) -> int:
        if len(position) != len(speed):
            return 0

        # Pair each car's position with its speed and sort by position in desc order
        cars = sorted(zip(position, speed), reverse=True)
        fleet_stack = []

        for pos, spd in cars:
            # Calculate the time to reach the target
            time_to_target = (target - pos) / spd

            # If the stack is not empty and the current car's time to target is less than
            # or equal to the top of the stack, it means this car will catch up to the
            # fleet represented by the top car
            if fleet_stack and time_to_target <= fleet_stack[-1]:
                continue

            # Otherwise, this car forms a new fleet
            fleet_stack.append(time_to_target)

        # The number of fleets is the number of unique times to target in the stack
        return len(fleet_stack)


# Create an instance of the class
solution = Solution()
