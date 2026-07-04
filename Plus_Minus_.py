def plusMinus(arr):
    length = len(arr)
    positive = [n for n in arr if n > 0]
    negative = [n for n in arr if n < 0]
    zero = [n for n in arr if n == 0]
    print(len(positive) / length)
    print(len(negative) / length)
    print(len(zero) / length)

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
