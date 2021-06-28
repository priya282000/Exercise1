""" User Details """
from insert_query import InsertQuery
from validate_fields import validate_methods
import logging

#pylint: disable=line-too-long
#pylint: disable=too-many-nested-blocks
#pylint: disable=too-many-branches
#pylint: disable=too-many-instance-attributes
#pylint: disable=too-many-statements
#pylint: disable=too-few-public-methods

logging.basicConfig(filename='file.log', level=logging.INFO,
                    format='%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')

class DetailsCheck():
    """ Input and validate """

    def __init__(self):
        """ Initialisation """
        self.fname = ''
        self.mname = ''
        self.lname = ''
        self.dob = ''
        self.gender = ''
        self.nationality = ''
        self.city = ''
        self. state = ''
        self.pincode = 0
        self.qualification = ''
        self.salary = 0.0
        self.pan = 0
        self.response = ''
        self.reason = ''
        self.flag = 0

    def input_values(self):
        """ input and check """
        first_name = input("First name : ")
        if len(first_name) > 0:
            self.fname = first_name
        if validate_methods().fname_validate(self.fname) == 'success':
            middle_name = input("Middle name : ")
            if len(middle_name) > 0:
                self.mname = middle_name
            if validate_methods().mname_validate(self.mname) == 'success':
                last_name = input("Last name : ")
                if len(last_name) > 0:
                    self.lname = last_name
                if validate_methods().lname_validate(self.lname) == 'success':
                    dob = input("DOB (YYYY-MM-DD) : ")
                    if len(dob) > 0:
                        self.dob = dob
                    if validate_methods().dob_validate(self.dob) == 'success':
                        gender = input("Gender : ")
                        if len(gender) > 0:
                            self.gender = gender
                        if validate_methods().gender_validate(self.gender) == 'success':
                            nationality = input("Nationality : ")
                            if len(nationality) > 0:
                                self.nationality = nationality
                            if validate_methods().nationality_validate(self.nationality) == 'success':
                                city = input("Current city : ")
                                if len(city):
                                    self.city = city
                                if validate_methods().city_validate(self.city) == 'success':
                                    state = input("State : ")
                                    if len(state):
                                        self.state = state
                                    if validate_methods().state_validate(self.state) == 'success':
                                        pincode = int(input("Pincode : "))
                                        if pincode > 0:
                                            self.pincode = pincode
                                        if validate_methods().pincode_validate(self.pincode) == 'success':
                                            qualification = input("Qualification : ")
                                            if len(qualification) > 0:
                                                self.qualification = qualification
                                            if validate_methods().qualification_validate(self.qualification) == 'success':
                                                salary = float(input("Salary : "))
                                                if salary > 0:
                                                    self.salary = salary
                                                if validate_methods().salary_validate(self.salary) == 'success':
                                                    pan = int(input("PAN number : "))
                                                    if pan > 0:
                                                        self.pan = pan
                                                    if validate_methods().pan_validate(self.pan) == 'success':
                                                        print("end")
                                                    else:
                                                        self.flag = 2
                                                        self.response = "validation error"
                                                        self.reason = validate_methods().pan_validate(self.pan)
                                                else:
                                                    self.flag = 2
                                                    self.response = "validation error"
                                                    self.reason = validate_methods().salary_validate(self.salary)
                                            else:
                                                self.flag = 2
                                                self.response = "validation error"
                                                self.reason = validate_methods().qualification_validate(self.qualification)

                                        else:
                                            self.flag = 2
                                            self.response = "validation error"
                                            self.reason = validate_methods().pincode_validate(self.pincode)

                                    else:
                                        self.flag = 2
                                        self.response = "validation error"
                                        self.reason = validate_methods().state_validate(self.state)

                                else:
                                    self.flag = 2
                                    self.response = "validation error"
                                    self.reason = validate_methods().city_validate(self.city)

                            else:
                                self.flag = 2
                                self.response = "validation error"
                                self.reason = validate_methods().nationality_validate(self.nationality)

                        else:
                            self.flag = 2
                            self.response = "validation error"
                            self.reason = validate_methods().gender_validate(self.gender)

                    else:
                        self.flag = 2
                        self.response = "validation error"
                        self.reason = validate_methods().dob_validate(self.dob)

                else:
                    self.flag = 2
                    self.response = "validation error"
                    self.reason = validate_methods().lname_validate(self.lname)

            else:
                self.flag = 2
                self.response = "validation error"
                self.reason = validate_methods().mname_validate(self.mname)

        else:
            self.flag = 2
            self.response = "validation error"
            self.reason = validate_methods().fname_validate(self.fname)


        if self.flag == 0:
            self.flag = 0
            if validate_methods().eligibility_age(self.gender, self.dob) == 'success':
                if validate_methods().eligibility_nation(self.nationality) == 'success':
                    if validate_methods().eligibility_state(self.state) == 'success':
                        if validate_methods().eligibility_salary(self.salary) == 'success':
                            self.flag = 0
                        else:
                            self.flag = 1
                            self.response = "Failed"
                            self.reason = validate_methods().eligibility_salary(self.salary)

                    else:
                        self.flag = 1
                        self.response = "Failed"
                        self.reason = validate_methods().eligibility_state(self.state)

                else:
                    self.flag = 1
                    self.response = "Failed"
                    self.reason = validate_methods().eligibility_nation(self.nationality)

            else:
                self.flag = 1
                self.response = "Failed"
                self.reason = validate_methods().eligibility_age(self.gender, self.dob)

        if self.flag == 0:
            self.flag = 0
            self.response = "Success"

        if self.flag <= 1:
            InsertQuery().insert_request(self.fname, self.mname, self.lname, self.dob, self.gender, self.nationality, self.city, self.state,self.pincode,self.qualification, self.salary, self.pan)
            InsertQuery().insert_response(self.response, self.reason, self.flag)

obj = DetailsCheck()
obj.input_values()
