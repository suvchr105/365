"""
Sum Pair closest to target
Difficulty: EasyAccuracy: 44.75%Submissions: 46K+Points: 2
Given an array arr[] and a number target, find a pair of elements (a, b) in arr[], where a<=b whose sum is closest to target.
Note: Return the pair in sorted order and if there are multiple such pairs return the pair with maximum absolute difference. If no such pair exists return an empty array.

Examples:

Input: arr[] = [10, 30, 20, 5], target = 25
Output: [5, 20]
Explanation: As 5 + 20 = 25 is closest to 25.
Input: arr[] = [5, 2, 7, 1, 4], target = 10
Output: [2, 7]
Explanation: As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and (4, 7) is 3. Hence, [2, 7] has maximum absolute difference and closest to target. 
Input: arr[] = [10], target = 10
Output: []
Explanation: As the input array has only 1 element, return an empty array.
Constraints:
1 <= arr.size() <= 2*105
0 <= target<= 2*105
0 <= arr[i] <= 105

"""
class Solution:
    def sumClosest(self, arr, target):
        if len(arr) < 2:
            return []
    
        # Sort the array
        arr.sort()
        n = len(arr)
    
        # Initialize variables
        left = 0
        right = n - 1
        closest_sum = float('inf')  # To track the closest sum
        result_pair = []
        max_abs_diff = -float('inf')  # To track the pair with maximum absolute difference
    
        # Two-pointer approach
        while left < right:
            # Calculate current sum
            current_sum = arr[left] + arr[right]
    
            # Update closest sum and result pair
            if abs(target - current_sum) < abs(target - closest_sum) or \
               (abs(target - current_sum) == abs(target - closest_sum) and (arr[right] - arr[left] > max_abs_diff)):
                closest_sum = current_sum
                result_pair = [arr[left], arr[right]]
                max_abs_diff = arr[right] - arr[left]
    
            # Move pointers
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # If we find the exact target, return the pair
                return [arr[left], arr[right]]
    
        return result_pair