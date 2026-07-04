def miniMaxSum(arr):
    sums = []
    for num in arr:
        array = arr.copy()
        array.remove(num)
        sums.append(sum(array))
    print(f"{min(sums)} {max(sums)}")

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
