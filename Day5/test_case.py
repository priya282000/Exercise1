import pytest
from validate_fields import validate_methods


@pytest.mark.parametrize("fname, output", [("priya","success"),("abcdef","success"),("","first name not filled"),("priya123","name should have only alphabets")])
def test_fname(fname, output):
    assert validate_methods().fname_validate(fname) == output

@pytest.mark.parametrize("mname, output",[("","success"),("123","name should have only alphabets"),("abc", "success")])
def test_mname(mname, output):
    assert validate_methods().mname_validate(mname) == output

@pytest.mark.parametrize("lname, output",[("","Last name not filled"),("123","name should have only alphabets"),("abc", "success")])
def test_mname(lname, output):
    assert validate_methods().lname_validate(lname) == output

@pytest.mark.parametrize("date, output",[("2000-12-28","success"),("28-11-2000","Invalid date")])
def test_date(date, output):
    assert validate_methods().dob_validate(date) == output

@pytest.mark.parametrize("gender, output",[("","Gender not filled"),("Female","success"),("123","Invalid gender")])
def test_gender(gender, output):
    assert validate_methods().gender_validate(gender) == output

@pytest.mark.parametrize("nation, output",[("","Nationality not filled"),("Indian","success"),("123","Invalid nationality")])
def test_nationality(nation, output):
    assert validate_methods().nationality_validate(nation) == output

@pytest.mark.parametrize("city, output",[("","City not filled"),("Coimbatore","success"),("123","Invalid city")])
def test_city(city, output):
    assert validate_methods().city_validate(city) == output

@pytest.mark.parametrize("state, output",[(""," State not filled"),("Tamil Nadu","success")])
def test_state(state, output):
    assert validate_methods().state_validate(state) == output

@pytest.mark.parametrize("pincode, output",[(0,"Pincode not filled"),(641025,"success"),("abc","Invalid pincode")])
def test_pincode(pincode, output):
    assert validate_methods().pincode_validate(pincode) == output

@pytest.mark.parametrize("qualification, output",[("","Qualification not filled"),("IT","success")])
def test_qualification(qualification, output):
    assert validate_methods().qualification_validate(qualification) == output

@pytest.mark.parametrize("pincode, output",[(0,"Pincode not filled"),(641025,"success"),("abc","Invalid pincode")])
def test_pincode(pincode, output):
    assert validate_methods().pincode_validate(pincode) == output

@pytest.mark.parametrize("salary, output",[(0.0,"Salary not filled"),(20000.0,"success"),("abc","Invalid salary")])
def test_salary(salary, output):
    assert validate_methods().salary_validate(salary) == output

@pytest.mark.parametrize("pan, output",[(0,"PAN number not filled"),(641025,"success"),("abc","Invalid PAN number")])
def test_pan(pan, output):
    assert validate_methods().pan_validate(pan) == output

@pytest.mark.parametrize("gender, date, output",[("Male","2000-11-28","Age is less than expected"),("Male","1990-11-28","success"),("Female", "2000-11-28","success"),("Female","2010-11-28","Age is less than expected")])
def test_age(gender, date, output):
    assert validate_methods().eligibility_age(gender, date) == output

@pytest.mark.parametrize("nationality, output",[("Indian","success"),("Chinese","Nationality criteria not satisfied")])
def test_nation(nationality, output):
    assert validate_methods().eligibility_nation(nationality) == output

@pytest.mark.parametrize("state, output",[("Tamil Nadu","success"),("Chinese","State criteria not satisfied")])
def test_state_criteria(state, output):
    assert validate_methods().eligibility_state(state) == output

@pytest.mark.parametrize("salary, output",[(20000,"success"),(9000,"Salary criteria not satisfied")])
def test_salary_criteria(salary, output):
    assert validate_methods().eligibility_salary(salary) == output