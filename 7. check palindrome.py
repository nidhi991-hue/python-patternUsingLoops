# Check whether a number is palindrome


n=12321
original=n
reverse=0

while n>0:
    digit =n % 10
    reverse = reverse * 10 +digit
    n//=10
    
if original == reverse:
    print("it is palindrome")
else:
    print("it's not palindrome")