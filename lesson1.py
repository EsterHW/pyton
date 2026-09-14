
# # תרגיל 1
# str = input("Enter  str: ")
# i = 0
# j = -1
# while i < len(str):
#     if str[i] != str[j]:
#         print("not philindrom")
#         break
#     j -= 1
#     i += 1
#
# if i == len(str):
#     print("yes philindrom")


# תרגיל 2
#
# str2 = input("Enter  str: ")
# i = 0
# count = 0
# while i < len(str2):
#    if str2[i] == " ":
#        count += 1
#    i += 1
#
# print("the count of words is: " )
# print(count + 1)

# תרגיל 3
str3 = input("Enter  str with more than 1 word ")
i = 0
temp = ""
while i < len(str3):
   if i == 0:
       temp += str3[i]
   elif str3[i] == " ":
       temp += str3[i+1]
   i += 1
print("the rashey teivot of the word is:")
print(temp)