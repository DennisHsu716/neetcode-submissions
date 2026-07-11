class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if slow == fast:
                break
            
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow 