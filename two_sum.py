class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = range(len(nums))

        original_pairs = [(nums[i], i) for i in length]

        sorted_nums = sorted(original_pairs, key=lambda x: x[0])

        for i in length:
            diff = target - sorted_nums[i][0]
            result = self.recursive(sorted_nums, diff)
            
            if result is None:
                continue

            return [sorted_nums[i][1], result]

    def recursive(self, nums: [(int, int)], diff: int) -> int|None:
        if len(nums) == 1:
            if diff == nums[0][0]:
                return nums[0][1]
            else:
                return None

        if nums[len(nums)//2][0] > diff:
            result = self.recursive(nums[0:len(nums)//2], diff)
        else:
            result = self.recursive(nums[len(nums)//2:len(nums)], diff)

        return result