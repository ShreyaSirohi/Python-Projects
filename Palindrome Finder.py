def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def find_palindrome(n):
    while not is_palindrome(n):
        n += 1
    return n

ask = int(input("Enter the number: "))

if is_palindrome(ask) == True:
    print("This number is a palindrome.")

else:
    a = find_palindrome(ask)
    print("The next palindrome is", a)
