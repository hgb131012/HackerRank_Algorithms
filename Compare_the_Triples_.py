import os

def compareTriplets(a, b):
    a_score = 0
    b_score = 0
    for x, y in zip(a, b):
        if x < y:
            b_score += 1
        if x > y:
            a_score += 1
    return [a_score, b_score]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
