# Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #initilize pointer k
        k = 0

        # iterate over nums array to find val
        for i in range(nums.length()):
            if nums[i] != val:
                #place it at kth position
                nums[k] = nums[i]
                k += 1
        
        return k
