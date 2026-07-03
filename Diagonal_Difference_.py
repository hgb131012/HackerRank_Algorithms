import os

def diagonalDifference(array):
    left_to_right = 0
    right_to_left = 0
    for index, arr in enumerate(array):
        left_to_right += arr[index]
    for index, arr in enumerate(array[::-1]):
        right_to_left += arr[index]
    return abs(left_to_right - right_to_left)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
