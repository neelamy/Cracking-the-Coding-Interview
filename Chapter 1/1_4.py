# Source : Palindrome Permuation

# Algo/DS : String

# Complexity : O(N)


def check(A):
	d = {}

	for i in A:
		d[i] = d.get(i,0) + 1

	flag = False

	for v in d:
		if v%2 != 0 and flag : return False
		if v%2 != 0 and not flag : flag = True

	return True


A = "Tact Coa"

print check(A)