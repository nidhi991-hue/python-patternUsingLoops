# # ----------------------
# # 1. Print "Hello, World!"
# print("hello world")
# # ----------------------
# # 2. Add two numbers
# a=10
# b=20
# print(a+b)
# # ----------------------
# # 3. Swap two numbers
# a=10
# b=20
# a,b=b,a
# print("a: ", a)
# print("b: ", b)
# # ----------------------
# # 4. Check whether a number is even or odd
# a=11
# if a%2==0:
#     print("a is even")
# else:
#     print("a is odd")
# # ----------------------
# # 5. Find the largest of two numbers
# a=10
# b=20
# if a>b:
#     print("a is greater than b")
# else:
#     print("b is greater than a")
# # ----------------------
# # 6. Find the largest of three numbers
# a=10
# b=20
# c=30
# if a>b and a>c:
#     print("a is greatest")
# elif b>a and b>c:
#     print("b is greatest")
# else:
#     print("c is greatest")
# # ----------------------
# # 7. Check whether a number is positive, negative, or zero
# a=10
# if a>0:
#     print("positive no.")
# elif a<0:
#     print("negative no.")
# else:
#     print("zero")
# # ----------------------
# # 8. Find the square and cube of a number
# a=10
# square=a*a
# cube=a*a*a
# print("Square of", a, "is:", square)
# print("Cube of", a, "is:", cube)
# # ----------------------
# # 9. Calculate the area of a circle
# radius=10
# pi=3.14
# print("Area of circle is:", pi*radius*radius)
# # ----------------------
# # 10. Convert Celsius to Fahrenheit
# Celsius = 20
# Fahrenheit = (Celsius*9/5)+32
# print(Fahrenheit)
# # ----------------------
# # 11. Print numbers from 1 to 10
# for i in range(1,11):
#     print(i)
# # ----------------------
# # 12. Find the sum of the first N natural numbers
# n=6
# total=0
# for i in range(1,n):
#     total+=i
# print(total)
# # ----------------------
# # 13. Find the factorial of a number
# fact=1
# for i in range(1, 6):
#     fact*=i
# print(fact)
# # ----------------------
# # 14. Print the multiplication table of a number
# n=4
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")
# # ----------------------
# # 15. Count the digits in a number
# n=123456745678
# count=0
# while n>0:
#     count+=1
#     n//=10
# print(count)
# # ----------------------
# # 16. Find the sum of the digits of a number
# n=12345
# sum=0
# while n>0:
#     digit=n%10
#     sum+=digit
#     n//=10
# print(sum)
# # ----------------------
# # 17. Reverse a number
# n=123456789
# reverse=0
# while n>0:
#     digit=n%10
#     reverse=reverse*10+digit
#     n//=10
# print(reverse)
# # ----------------------
# # 18. Check whether a number is a palindrome
# n=12321
# original=n
# reverse=0
# while n>0:
#     digit=n%10
#     reverse=reverse*10+digit
#     n//=10
# if original==reverse:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")
# # ----------------------
# # 19. Check whether a number is prime
# n=7
# if n<=1:
#     print("it is not prime number")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("it is not prime number")
#             break
#     else:
#         print("it is a prime number")
# # ----------------------
# 20. Print the Fibonacci series
n=10
a=0
b=1
count=0
while count<n:
    print(a, end=" ")
    c=a+b
    a=b
    b=c
    count+=1