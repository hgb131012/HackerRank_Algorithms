from collections import defaultdict
import os

def minimumDistances(arr):
    indices = defaultdict(list)
    for index, n in enumerate(arr):
        indices[n].append(index)
    pairs = {n: i for n, i in indices.items() if len(i) > 1}
    if len(pairs) == 0:
        return -1
    distances = []
    for p in pairs:
        distances.append(abs(pairs[p][0] - pairs[p][1]))
    return min(distances)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistances(a)
    fptr.write(str(result) + '\n')
    fptr.close()
