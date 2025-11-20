#Sum of first N natural numbers

def sum_natural(N):
    if N == 0:
        return 0  
    return N + sum_natural(N - 1)   

N= int(input())
print(sum_natural(N))
