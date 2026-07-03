import os

def aVeryBigSum(array):
    return sum(array)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
