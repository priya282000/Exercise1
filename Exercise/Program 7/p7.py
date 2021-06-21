try:
    try:
        name=input("Name : ")
        if not isinstance(name,str):
            raise TypeError("Name should contain only alphabets")
    except TypeError as e:
        print(e)
    try:
        age=int(input("Age : "))
        #check=isinstance(age,int)
        if not isinstance(age,int):
            raise TypeError("Age should contain only numbers")
    except TypeError as e:
        print(e)
    try:
        gender=input("Gender : ")
        if not isinstance(gender,str):
            raise TypeError("Gender should contain only alphabets")
    except TypeError as e:
        print(e)
    try:
        salary=float(input("Salary : "))
        if not isinstance(salary,float):
            raise TypeError("Salary should contain only floating point numbers")
    except TypeError as e:
        print(e)
    try:
        state=input("State : ")
        if not isinstance(state,str):
            raise TypeError("State should contain only alphabets")
    except TypeError as e:
        print(e)
    try:
        city=input("City : ")
        if not isinstance(city,str):
            raise TypeError("City should contain only alphabets")
    except TypeError as e:
        print(e)

    print("Name :",name,"\nAge :",age,"\nGender :",gender,"\nSalary :",salary,"\nState :",state,"\nCity :",city)
except Exception as e:
    print(e)
