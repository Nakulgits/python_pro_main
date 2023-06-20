# from ast import main


def fibo(a):
    if a<=0:
        print("Incorrect input")
    elif a==1:
        return 0
    elif a==2:
        return 1
    else:
        return fibo(a-1)+fibo(a-2)

def fact(b):
    if b==1 or b==0:
        return 1
    else:
        return b*fact(b-1)

def main():
    x=int(input('enter the nth term in the fibonacci series'))
    fibo(x)
    y=int(input('enter the number whose factorial need to be found'))
    fact(y) 

if(__name__=='__main__'):
    main()
