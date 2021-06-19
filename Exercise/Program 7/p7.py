try:
    name=input("Name : ")
    age=int(input("Age : "))
    gender=input("Gender : ")
    salary=float(input("Salary : "))
    state=input("State : ")
    city=input("City : ")
    print("Name :",name,"\nAge :",age,"\nGender :",gender,"\nSalary :",salary,"\nState :",state,"\nCity :",city)
except Exception as e:
    print(e)
