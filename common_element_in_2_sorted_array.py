'''
Source : CTCI

Problem : Given two sorted arrays, find the number of elements in common. The arrays are the same length
and each has all distinct elements

Algo/DS : linear search , array

Complexity : O(n)
'''

class common:

	def __init__(self, A, B):

		self.A = A

		self.B = B


	'''start with first element of both array. If elements are same, take it and increment both indexes.
	else increment the index of arry having lowest element.'''
	
	def find_common(self):

		index_A, index_B = 0 ,0

		length_of_array = len(self.A)

		common_element = []

		while (index_B < length_of_array  and index_A < length_of_array ):

			if self.A[index_A] == self.B[index_B]:

				common_element.append(self.A[index_A])

				index_A, index_B = index_A + 1, index_B + 1

			elif self.A[index_A] < self.B[index_B]:

				index_A = index_A + 1

			else :

				index_B = index_B + 1

		return common_element



def main():

	A = [13, 27, 35, 40, 49, 55, 59]

	B = [17, 35, 39, 40, 55, 58, 59]

	c = common(A, B)

	print c.find_common()



if __name__ == '__main__':

	main()