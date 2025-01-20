class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is an empty string, return 0
        if not needle:
            return 0
        
        # Iterate through the haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring matches the needle
            if haystack[i:i + len(needle)] == needle:
                return i
        
        # If needle is not found, return -1
        return -1

# Example usage:
solution = Solution()
haystack = "sadbutsad"
needle = "sad"
result = solution.strStr(haystack, needle)
print(f"First occurrence index: {result}")  # Output: 0
