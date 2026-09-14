# Print prime numbers from 1 to 50

n=50

for num in range(2, n+1):
    is_prime = True
    
    for i in range(2, num):
        if num % i ==0:
            is_prime=False
            break
        
    if is_prime:
        print(num, end= " ")
