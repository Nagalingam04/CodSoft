#addition 
def add(num1,num2):
    return num1+num2

#subtraction
def sub(num1,num2):
    return num1-num2

#multiply
def mul(num1,num2):
    return num1*num2

#division
def div(num1,num2):
    return num1/num2

#main

def main():
    print("Simple Calculator")
    print("\n1.Additon(+)\n2.Subtraction(-)\n3.Multiplication(*)\n4.Division(/)\n\nEnter Operator:")
    op=input()
    if op=="+":
        print("Enter First Number:")
        num1=int(input())
        print("Enter Second Number:")
        num2=int(input())
        print("After Addition:" ,add(num1,num2))
    elif op=="-":
        print("Enter First Number:")
        num1=int(input())
        print("Enter Second Number:")
        num2=int(input())
        print("After Subtraction:" ,sub(num1,num2))
    elif op=="*":
        print("Enter First Number:")
        num1=int(input())
        print("Enter Second Number:")
        num2=int(input())
        print("After Multiplication:" ,mul(num1,num2))
    elif op=="/":
        print("Enter Dividend:")
        num1=int(input())
        print("Enter Divisor:")
        num2=int(input())
        print("After Division:" ,div(num1,num2))


if __name__=="__main__":
    main()