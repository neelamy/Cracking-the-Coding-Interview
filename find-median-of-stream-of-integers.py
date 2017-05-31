# Source : http://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
		
# Explanation : http://www.ardendertat.com/2011/11/03/programming-interview-questions-13-median-of-integer-stream/

# Algo/DS : Heap

# Complexity : O(lg n)

import heapq

class streamMedian:

	def __init__(self):

 		self.max_heap , self.min_heap = [], []

		self. N = 0


	def insert(self,num):

		if self.N % 2 == 0:

			heapq.heappush(self.max_heap, -1* num)

			self.N +=1

			if len(self.min_heap) == 0 : 

				return

			else:

				if -1* self.max_heap[0] > self.min_heap[0]:

					to_min = -1 * heapq.heappop(self.max_heap)

					to_max = heapq.heappop(self.min_heap)

					heapq.heappush(self.max_heap, -1* to_max)

					heapq.heappush(self.min_heap, to_min)

		else:

			heapq.heappush(self.max_heap, -1* num)

			self.N +=1

			to_min = -1 * heapq.heappop(self.max_heap)

			heapq.heappush(self.min_heap, to_min)


	def find_median(self):

		if self.N % 2 == 0:

			return (-1* self.max_heap[0] + self.min_heap[0]) / 2.0

		else:

			return -1* self.max_heap[0] 


def main():

	s = streamMedian()

	array_of_numbers = [12, 4, 5, 3, 8, 7]

	for i in array_of_numbers:

		s.insert(i)

		print s.find_median(),

		

if __name__ == "__main__":
	main()
