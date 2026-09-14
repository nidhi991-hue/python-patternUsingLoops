# Check whether a number is prime

n=29
is_prime=True

if n<2:
    is_prime=False
    
else:
    for i in range(2,n):
        if n%i ==0:
            is_prime=False
            break
    
if is_prime:
    print("it is prime number")
else:
    print("it is not prime number")