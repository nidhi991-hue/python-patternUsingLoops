n=5

for i in range(n):
    
    value=1
    
    for j in range(i+1):
        print(value, end=" ")
        value=value*(i-j)//(j+1)
    print()