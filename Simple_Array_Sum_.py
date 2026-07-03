import os

def simpleArraySum(arr):
    return sum(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = simpleArraySum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
