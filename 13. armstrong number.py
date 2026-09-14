n=153
original=n
digits =0
temp=n

while temp>0:
    digits +=1
    temp //=10
    
total =0
temp=n

while temp>0:
    digits= temp % 10
    total+=digits**digits
    temp//=10
    
if total == original:
    print("Armstrong")
else:
    print("Not Armstrong")