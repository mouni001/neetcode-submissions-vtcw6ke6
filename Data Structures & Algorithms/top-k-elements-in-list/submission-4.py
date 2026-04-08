class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        min_heap = []

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1

        for number, freq in dictionary.items():
            heapq.heappush(min_heap, (freq, number))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
            print(min_heap)

        return [x2 for x1, x2 in min_heap]
        




