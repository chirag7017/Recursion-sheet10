# Reverse a string using recursion

def reverse_string(S):
    if len(S) <= 1:
        return S
    return S[-1] + reverse_string(S[:-1])
S = input()
print(reverse_string(S))
