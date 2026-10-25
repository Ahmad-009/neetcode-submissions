class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hash_lookup = {}

        for index,item in enumerate(nums):
            if item in hash_lookup:
                return True
            else:
                hash_lookup[item] = 1

        return False

        # for index,item in enumerate(nums):
        #     if item in nums[index + 1:]:
        #         return True
        # return False