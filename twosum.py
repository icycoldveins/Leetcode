# Given an array of integers nums and an
# integer target, return indices of the two
# numbers such that they add up to target.
# You may assume that each input would have exactly
# one solution, and you may not use the same element twice.
# You can return the answer in any order.

""" 
array of integers nums and
integer target
returned: indices of the two numbers that make it so it adds up to the target
assumption: each input has exactly one solution 

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

 """

# -> list[int]:
# the output of this function can only be a list which can take 
# only integer value
# else it will throw error 
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # self is the instance of the class
        # self.nums = nums
        # self.target = target
        # --> is a 
        for i in range(len(nums)):
            for j in range(i+1,(len(nums))):
                if nums[i]+nums[j]==target:
                    return[i,j]

nums = [2,7,11,15]
target = 9
solution = Solution()
print(solution.twoSum(nums,target))