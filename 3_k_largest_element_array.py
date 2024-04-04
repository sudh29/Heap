import heapq

class Solution:
	def kLargest(self,arr, n, k):
		max_heap = []
        heapq.heapify(max_heap)
        for i in range(n):
            heapq.heappush(max_heap, arr[i])
            if (len(max_heap) > k):
                heapq.heappop(max_heap)
        res = [i for i in max_heap]
        res = sorted(res,reverse=True)
	    return res
