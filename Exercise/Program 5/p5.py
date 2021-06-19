def binary(dec):
    try:
        if(dec>1):
            binary(dec//2)
        print(dec%2,end='')
    except Exception as e:
        print(e)

def octal(dec):
    try:
        if(dec>7):
            octal(dec//8)
        print(dec%8,end='')
    except Exception as e:
        print(e)

def hex(dec):
    try:
        if(dec>15):
            hex(dec//16)
        r=dec%16
        if r==10:
            print("A",end='')
        elif r==11:
            print("B",end='')
        elif r==12:
            print("C",end='')
        elif r==13:
            print("D",end='')
        elif r==14:
            print("E",end='')
        elif r==15:
            print("F",end='')
        else:
            print(r,end='')
    except Exception as e:
        print(e)

try:
    decimal=int(input("Enter a decimal value : "))
    print("Binary equivalent of",decimal,": ",end='')
    binary(decimal)
    print("\nOctal equivalent of",decimal,": ",end='')
    octal(decimal)
    print("\nHexadecimal equivalent of",decimal,": ",end='')
    hex(decimal)
except Exception as e:
    print(e)