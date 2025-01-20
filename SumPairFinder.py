class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store the number and its index
        num_map = {}
        
        # Iterate over the array
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement exists in the hash map
            if complement in num_map:
                return [num_map[complement], i]
            
            # If complement doesn't exist, add the current number and its index to the map
            num_map[num] = i
