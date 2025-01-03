
"""
Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.

Examples: 

Input: arr[] = [4, 2, 2, 6, 4], k = 6
Output: 4
Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6]. Hence, the answer is 4.
Input: arr[] = [5, 6, 7, 8, 9], k = 5
Output: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]. Hence, the answer is 2.
Input: arr[] = [1, 1, 1, 1], k = 0
Output: 4
Explanation: The subarrays are [1, 1], [1, 1], [1, 1] and [1, 1, 1, 1].
Constraints:

1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤105
0 ≤ k ≤ 105

"""


class Solution:
    def subarrayXor(self, arr, k):
        prefixXOR = 0
        xorCount = {}
        xorCount[0] = 1  # To handle subarrays starting from index 0
        count = 0
        
        for num in arr:
            prefixXOR ^= num
            # Check if there is a prefix XOR that satisfies the condition
            if prefixXOR ^ k in xorCount:
                count += xorCount[prefixXOR ^ k]
            # Update the frequency of the current prefix XOR
            xorCount[prefixXOR] = xorCount.get(prefixXOR, 0) + 1
        
        return count
    
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends