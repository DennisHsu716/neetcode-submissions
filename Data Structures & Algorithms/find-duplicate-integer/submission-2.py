class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow] 
            fast = nums[nums[fast]]

            if fast == slow:
                break 
        slow = 0 
        
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow 
