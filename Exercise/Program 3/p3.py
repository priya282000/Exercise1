import threading
import _thread
import time

def find_prime(n):
    try:
        flag=1
        for i in range(2,n//2+1):
            if n%i==0:
                flag=0
                break
        if flag==0:
            return 1
        else:
            return 0
    except Exception as e:
        print(e)

try:
    lim=int(input("Enter the limit : "))
    for i in range(2,lim):
        temp=find_prime(i)
        if temp==0:
            time.sleep(5)
            print(i," ")
except Exception as e:
    print(e)