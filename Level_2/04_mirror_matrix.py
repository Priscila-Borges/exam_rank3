"""
Given a 2D matrix (list of lists), return a new matrix where each row
is reversed.

Function signature
def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
"""

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
	rev_list = []

	for array in matrix:
		rev_list.append(array[::-1])

	return rev_list

print(mirror_matrix([[1,2,3],[4,5,6]]))
print(mirror_matrix([[1,2],[3,4],[5,6]]))
print(mirror_matrix([[7]]))
print(mirror_matrix([[1,2,3,4]]))
