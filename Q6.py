# Sum of digits of a number

def sum_of_digits(N):
    if N == 0:
        return 0
    return (N % 10) + sum_of_digits(N // 10)

N = int(input())
print(sum_of_digits(N))
