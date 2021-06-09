# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
         # [ 1, 2, 3] array input
         # [ 1, 2] continguous subarray 
         # [ 1, 3] subarray, but not contiguous
         # 6 expected output
         # contiguous subarray sums:
         # 1, 2, 3 = 6
         # 1, 2 = 3
         # 2, 3 = 5
         
        # 1. access the length of the array
        arr_len = len(nums) # 3
        # 2. final value -- DP here: we are "caching" a value and updating it
        max_sum = nums[0] # 1 
        # 3. intermediate value
        temp_sum = nums[0] # 1
        
        # 4. loop, using range() here, but you can iterate in different ways
        for i in range(1, arr_len):
            num = nums[i] # 3 --> 2
            # 5. within loop, max or min: MAX below 
            # 6. you'll usually have at least two of these
            # FYI: contiguous = either the number by itself is larger
            #      or all the numbers before it PLUS the number are larger
            
            # 7. start resetting for the next loop
            #    reset the temp_sum: will change
            #    reset the max_sum: may or may not change
            
            # -- DP below: we are repeating a mathematical equation
            #.   to find out answer
            # MAX 1
            # max(3, 3 + 3 = 6) --> max(2, 1 + 2 = 3)
            temp_sum = max(num, temp_sum + num) # 6 --> 3
            # MAX 2
            # max(6, 3) --> max(1, 3)
            max_sum = max(temp_sum, max_sum) # 6 --> 3
