# Count digits in a number

def count_digits(N):
    if N == 0:
        return 0
    return 1 + count_digits(N // 10)
N = int(input())
if N == 0:
    print(1)
else:
    print(count_digits(N))
