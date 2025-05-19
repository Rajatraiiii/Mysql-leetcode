class Solution(object):
    def triangleType(self, nums):
        # Sort the sides to simplify inequality checks
        nums.sort()
        
        # Check for triangle inequality
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        
        # Classify based on side lengths
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return "isosceles"
        else:
            return "scalene"
