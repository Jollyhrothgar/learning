#!/usr/bin/env python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final_map = {}
        missing_number = 0
        for num in nums:
            if num not in final_map:
                final_map[num] = 1
            else:
                final_map[num] += 1
        return sorted(final_map,key=final_map.get)[0]

s = Solution()
test_set = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]
print s.singleNumber(test_set)
