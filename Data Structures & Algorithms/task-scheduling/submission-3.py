class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-val for val in count.values()]
        heapq.heapify(heap)
        quene = deque()
        time = 0
        ava_time = 0
        remain = 0

        while heap or quene:
            time += 1
            if heap:
                a = heapq.heappop(heap)
                a += 1
                if a != 0:
                    quene.append((time + n, a))
            
            if quene and quene[0][0] == time:
                ava_time, remain = quene.popleft()
                heapq.heappush(heap, remain)
        return time 
