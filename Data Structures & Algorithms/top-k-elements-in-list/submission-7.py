import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #min heap
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        heap = []
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        answer = []
        for frequency, num in heap:
            answer.append(num)


        return answer

            