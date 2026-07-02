class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        
        #first lap, slow:1 fast:2
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
        #if fast = slow -> go, no break 
            if fast == slow:
                break
        
        #second lap, slow back, and both move one step, meet return 
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow 