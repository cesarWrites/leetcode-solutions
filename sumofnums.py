class Solution(object):
    def twoSum(nums, target):
        arr_len = len(nums)
        for i in range(arr_len):
                for j in range(arr_len):
                    if((nums[i] + nums[j]) == target):
                        return [i,j]       
print(Solution.twoSum(nums = [2,7,11,15], target = 9))

