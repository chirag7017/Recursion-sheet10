# Print numbers from 1 to N

def print_numbers(N):
    if N == 0:
        return
    print_numbers(N - 1)
    print(N, end=" ")

N = int(input())
print_numbers(N)
