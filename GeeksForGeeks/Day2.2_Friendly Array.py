"""
Friendly Array
Difficulty: BasicAccuracy: 59.32%Submissions: 7K+Points: 1
Numbers have a measure of friendliness defined as the absolute difference between them. Given an circular array of integers arr[], calculate the friendliness of the array. Friendliness is the sum of the absolute differences between each element and its closest friend in the array.

Examples:

Input: arr[] = [4, 1, 5]
Output: 8
Explanation: The sum of absolute differences with closest neighbors is |4-1| + |1-5| + |5-4| = 8.
Input: arr[] = [1, 1, 1]
Output: 0
Explanation: All elements are identical, so the sum of differences is zero.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
2 < arr.size() ≤ 106
1 ≤ arr[i] ≤ 105

"""

# Solution:

def calculateFriendliness(arr):
    n = len(arr)
    friendliness = 0

    for i in range(n):
        # Neighbors in a circular array
        prev = arr[(i - 1) % n]
        next_ = arr[(i + 1) % n]
        
        # Add both differences
        friendliness += abs(arr[i] - prev) + abs(arr[i] - next_)
    
    # Each difference is counted twice (once for each neighbor), so divide by 2
    return friendliness // 2