class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0

        #first lap, mvoe both fast 2 and slow 1,
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break
        
        slow = 0
        #second lap, both move 1, if met return 
        while slow != fast:
            fast = nums[fast] 
            slow = nums[slow]
        return slow 