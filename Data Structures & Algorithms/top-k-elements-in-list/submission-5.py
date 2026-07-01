class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}

        for i in range(len(nums)):
            n = nums[i]
            if n not in count:
                count[n] = 0
            count[n] += 1
        
        sorted_item = sorted(count.items(), key=lambda item:item[1], reverse = True)

        for item in sorted_item[:k]:
            res.append(item[0])
        return res 