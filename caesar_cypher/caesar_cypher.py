# this is just below is the function with parameters and arguments calculation 
# this is the function with the positional arguments

# name ='nakul'
# age =25.6756
# city ='amritsar'

# print(f"hello {name}")
# print(f"this is the ap[rrox my age is {age:.2f}")

# def printing_function(name,age):
#     print(f"my name is {name}")
#     print(f"the age is {age:.3f}")

# print("\n")
# printing_function(age=45.6778,name='ikshita dolly')
# -------------------------------------------------------------------



#-----------------------------------------------------------------------

# this is below the function for the calculating the cans if the area to be painted is given 

# given is formula = (wall height * wall width)/ coverage per can  

# wall_height=int(input("height of wall : "))
# wall_width=int(input("width of wall : "))
# coverage_per_can=int(input("the coverage per can is : "))

# def paint_cans_calculator(h,w,c):
#     return (h*w)/c
# import math
# print("the total cans that will be required are : ",math.ceil(paint_cans_calculator(h=wall_height,w=wall_width,c=coverage_per_can)))

# here i can use the round function or the math.ceil function
# ------------------------------------------------------------------------


#---------------------------------------------------------------------------------------

# this the function for checking the prime numbers calculation 

# def prime_checker(n):
#     if n==1:
#         return False
#     elif n>=2:
#         for i in range(2,int(n**0.5)+1):
#             if n%i==0:
#                 return False
#     return True

# number=17
# if prime_checker(number):
#     print(f"{number} is a prime number ")
# else:
#     print(f"{number} is not a prime number")

#-------------------------------------------------------------------------


#------------------------------------------------------------------------
# CAESAR CIPHER PART 1 
#------------------------------------------------------------------------

import string 
letters=string.ascii_letters
print(letters)
import art
#--------------------------------------- below is the code containing both the functions separately called --------------

# def encryption(the_input,shifts,new):
#     for character in the_input:
#         # for letter in letters:
#         if character in letters:
#                 # print("\nthe old letter is ", character)
#             ascii = ord(character)
#             if(ascii>=97 and ascii<=122):
#                 shifted_ascii = ((ascii - ord('a')) + shifts) % 26 + ord('a')
#             elif(ascii>=65 and ascii<=90):
#                 shifted_ascii = ((ascii - ord('A')) + shifts) % 26 + ord('A')
#             character = chr(shifted_ascii)
#             new.append(character)
#                 # print("\nthe new letter is ", ncharacter)
#     return new

# print("welcme to the cesar cipher game ")
# print("enter the string to be encrypted")
# the_input=input("enter the text below : ")
# print("enter the no of shifts to be done below")
# shifts=int(input("the no of shifts are "))
# new=[]
# encrypted_string = ''.join(encryption(the_input,shifts,new))
# print("the new string is ",encrypted_string)

# def decryption(encrypted_string,shifts,newd):
#     for character in encrypted_string:
#         # for letter in letters:
#         if character in letters:
#                 # print("\nthe old letter is ", character)
#             ascii = ord(character)
#             if(ascii>=97 and ascii<=122):
#                 shifted_ascii = ((ascii - ord('a')) - shifts) % 26 + ord('a')
#             elif(ascii>=65 and ascii<=90):
#                 shifted_ascii = ((ascii - ord('A')) - shifts) % 26 + ord('A')
#             character = chr(shifted_ascii)
#             newd.append(character)
#                 # print("\nthe new letter is ", ncharacter)
#     return newd

# newd=[]
# print("enter the no of shifts to be done below")
# shiftsd=int(input("the no of shifts are "))
# decrypted_string= ''.join(decryption(encrypted_string=encrypted_string,shifts=shiftsd,newd=newd))
# print("the new decrypted string is ",decrypted_string)

# ------------------------------------------------------------------------------------------------------

# -------------------------- below is the combination of these above encryption and decryption functions 
print(art.logo)
def caesar(the_input,shifts,direction):
    new=[]
    if direction=="encrypt":
        for character in the_input:
        # for letter in letters:
            if character in letters:
                # print("\nthe old letter is ", character)
                ascii = ord(character)
                if(ascii>=97 and ascii<=122):
                    shifted_ascii = ((ascii - ord('a')) + shifts) % 26 + ord('a')
                elif(ascii>=65 and ascii<=90):
                    shifted_ascii = ((ascii - ord('A')) + shifts) % 26 + ord('A')
                character = chr(shifted_ascii)
                new.append(character)
    elif direction=="decrypt":
        for character in the_input:
        # for letter in letters:
            if character in letters:
                    # print("\nthe old letter is ", character)
                ascii = ord(character)
                if(ascii>=97 and ascii<=122):
                    shifted_ascii = ((ascii - ord('a')) - shifts) % 26 + ord('a')
                elif(ascii>=65 and ascii<=90):
                    shifted_ascii = ((ascii - ord('A')) - shifts) % 26 + ord('A')
                character = chr(shifted_ascii)
                new.append(character)
    else:
        print("please enter the right direction")
    return new
while True:
    print("enter the string to be encrypted or decrypted \n")
    input_given=input()
    print("enter the string direction encrypt or decrypt \n")
    direction=input()
    print("enter the shifts \n")
    shifts=int(input())
    print(''.join(caesar(the_input=input_given,shifts=shifts,direction=direction)))
    print("press yes to continue and no to discontinue")
    the_reply=input()
    if the_reply=='yes':
        continue
    else:
        break