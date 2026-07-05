import os

def findDigits(num):
    count = 0
    for digit in str(num):
        if digit != "0" and num % int(digit) == 0:
            count = count + 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = findDigits(n)
        fptr.write(str(result) + '\n')
    fptr.close()
