from sys import stdin
from collections import Counter
from operator import itemgetter

min_, max_ = (int(x) for x in stdin.readline().split())

for line in stdin.readlines():
    filtered = list(filter(lambda x: min_ <= x <= max_, map(int, line.split())))
    if not filtered:
        print("-1")
    else:
        counted = Counter(filtered).most_common()
        max_count = max(counted, key=itemgetter(1))[1]
        print(max(map(lambda x: x[0], filter(lambda y: y[1] == max_count, counted))))




