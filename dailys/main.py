from itertools import pairwise




logs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for t0, t1 in pairwise(logs):
    print(t0, t1)
