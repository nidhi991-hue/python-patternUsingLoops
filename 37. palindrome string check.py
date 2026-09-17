s="madam"

reverse=""

for i in range(len(s) -1,-1,-1):
    reverse +=s[i]
    
if s==reverse:
    print("It's a Palindrome")
else:
    print("Not Palindrome")