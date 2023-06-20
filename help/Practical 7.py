
def length():#length of string.
    str1=input("Enter a string :")
    c=0
    for i in range(0,len(str1)):
        c+=1
    return c

def maximum(): #maximum of three strings.
    s1=input("Enter the first string :")
    s2=input("Enter the second string :")
    s3=input("Enter the third string :")
    m=max(s1,s2,s3)
    return m
      
def replace(): #replace all vowels with “#”.
    str1=input("Enter a string :")
    l=list(str1)
    for i in range(len(l)):
        if l[i] in ["a","i","e","o","u"]:
            l[i]="#"
    s = "".join(l)
    print("The given string is <{}>. The new string is <{}>".format(str1,s))
    

def word(): # number of words in the given string.
    str1=input("Enter a string :")
    l=str1.split()
    n=0
    for i in range(0,len(l)):
        n+=1
    return n

def palindrome(): #string is a palindrome or not.
    str1=input("Enter a string :")
    for i in range(0,int(len(str1)/2)):
         if str1[i] != str1[len(str1)-i-1]:
            return False
    return True

def main():
    while True:
        print("\n")
        print('''Choose :-
          1. to find the length of string
          2. to return the maximum string
          3. to replace vowel by # of a string
          4. to find the number of words in a string
          5. to check a string is palindrome or not
          6. to exit''')
        print("---------------------*******------------------------\n")
        ch=int(input("Enter your choice :"))
        
        if ch==1: 
            a=length()
            print("Length of given string is ",a)
        elif ch==2:
            b=maximum()
            print("Maximum string out of three is ",b)
        elif ch==3:
            c=replace()      
        elif ch==4:
            d=word()
            print("The number of word in given string is ",d)
        elif ch==5:
            e=palindrome()
            print("The given string is a palindrome : ",e)           
        elif ch==6 :
           print("Thank You !!!")
           break
        
main()


