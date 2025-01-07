"""
You are given an integer target and an array arr[]. You have to find number of pairs in arr[] which sums up to target. It is given that the elements of the arr[] are in sorted order.
Note: pairs should have elements of distinct indexes. 

Examples :

Input: arr[] = [-1, 1, 5, 5, 7], target = 6
Output: 3
Explanation: There are 3 pairs which sum up to 6 : {1, 5}, {1, 5} and {-1, 7}.
Input: arr[] = [1, 1, 1, 1], target = 2
Output: 6
Explanation: There are 6 pairs which sum up to 2 : {1, 1}, {1, 1}, {1, 1}, {1, 1}, {1, 1} and {1, 1}.
Input: arr[] = [-1, 10, 10, 12, 15], target = 125
Output: 0
Explanation: There is no such pair which sums up to 4.
Constraints:
-105 <= target <=105
 2 <= arr.size() <= 105
-105 <= arr[i] <= 105

"""

class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        left, right = 0, len(arr) - 1
        count = 0
    
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                if arr[left] == arr[right]:  # Special case: duplicates
                    n = right - left + 1
                    count += (n * (n - 1)) // 2
                    break
                else:
                    left_count, right_count = 1, 1
                    while left + 1 < right and arr[left] == arr[left + 1]:
                        left += 1
                        left_count += 1
                    while right - 1 > left and arr[right] == arr[right - 1]:
                        right -= 1
                        right_count += 1
                    count += left_count * right_count
                    left += 1
                    right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
        return count