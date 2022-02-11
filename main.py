# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def maxSubArray(self, nums) -> int:
        sum = -10**4
        savedPath = 0
        intermediateSum = -10**4
        for i in range(0, len(nums)):
            if intermediateSum > 0 and intermediateSum + nums[i] > sum and intermediateSum + nums[i] > sum + savedPath + nums[i]:
                sum = intermediateSum + nums[i]
                savedPath = 0
                intermediateSum = -10**4
                continue
            if sum < nums[i]:
                if sum + savedPath < 0:
                    sum = nums[i]
                else:
                    sum += nums[i] + savedPath
                savedPath = 0
                continue
            if nums[i] > 0:
                if intermediateSum < 0:
                    intermediateSum = nums[i]
                else:
                    intermediateSum += nums[i]
                if savedPath != 0:
                    if savedPath + nums[i] >= 0:
                        sum += savedPath + nums[i]
                        savedPath = 0
                    else:
                        savedPath += nums[i]
                else:
                    sum += nums[i]
            else:
                savedPath += nums[i]
                if intermediateSum > 0:
                    intermediateSum += nums[i]
                    if intermediateSum < 0:
                        intermediateSum = -10**4
        return sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.maxSubArray([0, -3, -6, 2, 7, -9, 3, -2, -2, -5, -4, 2, 4, -3, 7, 3, 9, -9]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
