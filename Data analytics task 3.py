E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}
union = E.union(N)
intersection = E.intersection(N)
difference = E - N
symmetric_difference = union - intersection
print('Union of E and N is: ')
print(union)
print('Intersection of E and N is: ')
print(intersection)
print('Difference of E and N is: ')
print(difference)
print('Symmetric difference of E and N is: ')
print(symmetric_difference)
