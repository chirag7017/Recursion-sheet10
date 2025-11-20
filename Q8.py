# Check if a string is a palindrome

def is_palindrome(S):
    if len(S) <= 1:
        return True
    if S[0] != S[-1]:
        return False
    return is_palindrome(S[1:-1])

S = input()
if is_palindrome(S):
    print("Palindrome")
else:
    print("Not Palindrome")
