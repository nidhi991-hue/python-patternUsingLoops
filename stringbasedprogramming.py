########################################
######## String-Based Problems #########
########################################
# # ----------------------------------------
# # 21. Reverse a string
# str = "python"
# print(str[::-1])
# # ----------------------------------------
# # 22. Check whether a string is a palindrome
# str="madam"
# reverse= ""

# for char in str:
#     reverse=reverse+char
    
# if reverse==str:
#     print("its palindrome")
# else:
#     print("not palindrome")
# # ----------------------------------------
# # 23. Count vowels in a string
# str = "Hello World!"
# count = 0

# for char in str:
#     if char in "aeiouAEIOU":
#         count+=1
# print(count)
# # ----------------------------------------
# # 24. Count vowels and consonants
# str="Hello World!"
# vowels=0
# consonents=0

# for char in str:
#     if char in "aeiouAEIOU":
#         vowels+=1
#     else:
#         consonents+=1
# print("No. of Vowels is: ", vowels)
# print("No. of consonents is: ", consonents)
# # ----------------------------------------
# # 25. Count the number of words in a string

# str="Python is very easy to learn"
# words= str.split()
# count= len(words)
# print("Total no. of words is: ", count)
# # ----------------------------------------
# # 26. Count the frequency of each character
# str= "hello world"
# frequency = {}

# for char in str:
#     if char in frequency:
#         frequency[char]+=1
#     else:
#         frequency[char]=1
# print(frequency)
# # ----------------------------------------
# # 27. Remove spaces from a string
# str= "hello world"
# result=""

# for char in str:
#     if char!=" ":
#         result+=char
# print(result)
# # ----------------------------------------
# # 28. Check whether two strings are anagrams

# # str1="hindi"
# # str2="nidhi"
# str1= input("enter first string: ")
# str2 = input("enter second string: ")
# if sorted(str1)==sorted(str2):
#     print("its anagram")
# else:
#     print("not anagram")
# # ----------------------------------------
# # 29. Find the first non-repeating character(unique)
# str= input("Enter string: ")

# for char in str:
#     if str.count(char)==1:
#         print("here is the first non-repeating character: ",char)
#         break
# else:
#     print("no repeating character found")
# # ----------------------------------------
# # 30. Convert the first letter of each word to uppercase
# str=input("enter the string: ")
# print(str.title())