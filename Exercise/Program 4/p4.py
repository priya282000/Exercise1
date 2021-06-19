def HCF(x,y):
    try:
        if(x>y):
            temp=y
        else:
            temp=x
        for i in range(1,temp):
            if((x%i==0)and(y%i==0)):
                hcf=i
        return hcf
    except Exception as e:
        print(e)

try:
    input1=int(input("Enter a number : "))
    input2=int(input("Enter another number : "))
    if(input1<0 or input2<0):
        raise ArithmeticError
    print("HCF or GCD of",input1,"and",input2,"is",HCF(input1,input2))
except ArithmeticError:
    print("Enter positive value")




