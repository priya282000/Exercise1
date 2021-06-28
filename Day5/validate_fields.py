""" Validate fields """
from datetime import datetime, date


class validate_methods():

    def fname_validate(self, fname):
        if len(fname)==0:
            return 'first name not filled'
        if isinstance(fname, str):
            if fname.isalpha():
                return 'success'
        return 'name should have only alphabets'

    def mname_validate(self, mname):
        if len(mname) == 0:
            return 'success'
        if isinstance(mname, str):
            if mname.isalpha():
                return 'success'
        return 'name should have only alphabets'

    def lname_validate(self, lname):
        if len(lname)==0:
            return 'Last name not filled'
        if isinstance(lname, str):
            if lname.isalpha():
                return 'success'
        return 'name should have only alphabets'

    def dob_validate(self, dob):
        try:
            if datetime.strptime(dob, "%Y-%m-%d").date():
                return 'success'
        except:
            return 'Invalid date'

    def gender_validate(self, gender):
        if len(gender) == 0:
            return 'Gender not filled'
        if isinstance(gender, str):
            if gender.isalpha():
                return 'success'
        return 'Invalid gender'

    def nationality_validate(self, nationality):
        if len(nationality) == 0:
            return 'Nationality not filled'
        if isinstance(nationality, str):
            if nationality.isalpha():
                return 'success'
        return 'Invalid nationality'

    def city_validate(self, city):
        if len(city) == 0:
            return 'City not filled'
        if isinstance(city, str):
            if city.isalpha():
                return 'success'
        return 'Invalid city'

    def state_validate(self, state):
        if len(state) == 0:
            return ' State not filled'
        if isinstance(state, str):
            return 'success'
        return 'Invalid state'

    def pincode_validate(self, pincode):
        if pincode == 0:
            return 'Pincode not filled'
        if isinstance(pincode, int):
            return 'success'
        return 'Invalid pincode'

    def qualification_validate(self, qualification):
        if len(qualification) == 0:
            return 'Qualification not filled'
        return 'success'

    def salary_validate(self, salary):
        if salary == 0.0:
            return 'Salary not filled'
        if isinstance(salary, float):
            return 'success'
        return 'Invalid salary'

    def pan_validate(self, pan_number):
        if pan_number == 0:
            return 'PAN number not filled'
        if isinstance(pan_number, int):
            return 'success'
        return 'Invalid PAN number'

    def eligibility_age(self, gender, dob):
        dob1 = datetime.strptime(dob, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - dob1.year - ((today.month, today.day) <
                                        (dob1.month, dob1.day))
        if gender == 'Male':
            if age > 21:
                return 'success'

        else:
            if age > 18:
                return 'success'
        return 'Age is less than expected'

    def eligibility_nation(self, nationality):
        if nationality == 'Indian' or nationality == 'American':
            return 'success'
        return 'Nationality criteria not satisfied'

    def eligibility_state(self, state):
        state_list = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',  'Chhattisgarh',  'Karnataka',  'Madhya Pradesh',  'Odisha',  'Tamil Nadu',  'Telangana', 'West Bengal']
        if state in state_list:
            return 'success'
        return 'State criteria not satisfied'

    def eligibility_salary(self, salary):
        if salary > 10000 and salary < 90000:
            return 'success'
        return 'Salary criteria not satisfied'

