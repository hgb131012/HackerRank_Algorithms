import os

def introTutorial(val, arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            left = left + 1
        else:
            right = mid - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    val = int(input().strip())
    num = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = introTutorial(val, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
