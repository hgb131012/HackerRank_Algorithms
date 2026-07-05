import os

def camelcase(s):
    return len([c for c in s if c.isupper()]) + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input().strip()
    result = camelcase(s)
    fptr.write(str(result) + '\n')
    fptr.close()
