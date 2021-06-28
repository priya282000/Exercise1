import pytest
import unittest
from validate_fields import *

class TestUser(unittest.TestCase):
    def test_fname_success(self):
        t1 = validate_methods().fname_validate("priya")
        self.assertEqual(t1, "success")

    def test_fname_empty(self):
        t1 = validate_methods().fname_validate("")
        self.assertEqual(t1, "first name not filled")

    def test_fname_invalid(self):
        t1 = validate_methods().fname_validate("1234")
        self.assertEqual(t1, "name should have only alphabets")

    def test_mname_success(self):
        t1 = validate_methods().mname_validate("priya")
        self.assertEqual(t1, "success")

    def test_mname_empty(self):
        t1 = validate_methods().mname_validate("")
        self.assertEqual(t1, "success")

    def test_mname_invalid(self):
        t1 = validate_methods().mname_validate("123")
        self.assertEqual(t1, "name should have only alphabets")

    def test_lname_success(self):
        t1 = validate_methods().lname_validate("priya")
        self.assertEqual(t1, "success")

    def test_lname_empty(self):
        t1 = validate_methods().lname_validate("")
        self.assertEqual(t1, "Last name not filled")

    def test_lname_invalid(self):
        t1 = validate_methods().lname_validate("123")
        self.assertEqual(t1, "name should have only alphabets")

    def test_date_success(self):
        t1 = validate_methods().dob_validate("2000-11-28")
        self.assertEqual(t1, "success")

    def test_date_invalid(self):
        t1 = validate_methods().dob_validate("28-11-2000")
        self.assertEqual(t1, "Invalid date")

    def test_gender_success(self):
        t1 = validate_methods().gender_validate("Female")
        self.assertEqual(t1, "success")

    def test_gender_invalid(self):
        t1 = validate_methods().gender_validate("123")
        self.assertEqual(t1, "Invalid gender")

    def test_gender_empty(self):
        t1 = validate_methods().gender_validate("")
        self.assertEqual(t1, "Gender not filled")

    def test_nationality_success(self):
        t1 = validate_methods().nationality_validate("Indian")
        self.assertEqual(t1, "success")

    def test_nationality_empty(self):
        t1 = validate_methods().nationality_validate("")
        self.assertEqual(t1, "Nationality not filled")

    def test_nationality_invalid(self):
        t1 = validate_methods().nationality_validate("123")
        self.assertEqual(t1, "Invalid nationality")

    def test_city_success(self):
        t1 = validate_methods().city_validate("Coimbatore")
        self.assertEqual(t1, "success")

    def test_city_empty(self):
        t1 = validate_methods().city_validate("")
        self.assertEqual(t1, "City not filled")

    def test_city_invalid(self):
        t1 = validate_methods().city_validate("123")
        self.assertEqual(t1, "Invalid city")

    def test_state_success(self):
        t1 = validate_methods().state_validate("Tamil Nadu")
        self.assertEqual(t1, "success")

    def test_state_empty(self):
        t1 = validate_methods().state_validate("")
        self.assertEqual(t1, " State not filled")

    def test_pincode_success(self):
        t1 = validate_methods().pincode_validate(641025)
        self.assertEqual(t1, "success")

    def test_pincode_empty(self):
        t1 = validate_methods().pincode_validate(0)
        self.assertEqual(t1, "Pincode not filled")

    def test_pincode_invalid(self):
        t1 = validate_methods().pincode_validate("abc")
        self.assertEqual(t1, "Invalid pincode")

    def test_qualification_success(self):
        t1 = validate_methods().qualification_validate("IT")
        self.assertEqual(t1, "success")

    def test_qualification_empty(self):
        t1 = validate_methods().qualification_validate("")
        self.assertEqual(t1, "Qualification not filled")

    def test_salary_success(self):
        t1 = validate_methods().salary_validate(20000.0)
        self.assertEqual(t1, "success")

    def test_salary_empty(self):
        t1 = validate_methods().salary_validate(0.0)
        self.assertEqual(t1, "Salary not filled")

    def test_salary_invalid(self):
        t1 = validate_methods().salary_validate("abc")
        self.assertEqual(t1, "Invalid salary")

    def test_pan_success(self):
        t1 = validate_methods().pan_validate(34567)
        self.assertEqual(t1, "success")

    def test_pan_empty(self):
        t1 = validate_methods().pan_validate(0)
        self.assertEqual(t1, "PAN number not filled")

    def test_pan_invalid(self):
        t1 = validate_methods().pan_validate("abc")
        self.assertEqual(t1, "Invalid PAN number")

    def test_age_fsuccess(self):
        t1 = validate_methods().eligibility_age("Female", "2000-11-28")
        self.assertEqual(t1, "success")

    def test_age_msuccess(self):
        t1 = validate_methods().eligibility_age("Male", "1990-11-28")
        self.assertEqual(t1, "success")

    def test_age_ffail(self):
        t1 = validate_methods().eligibility_age("Female", "2005-11-28")
        self.assertEqual(t1, "Age is less than expected")

    def test_age_mfail(self):
        t1 = validate_methods().eligibility_age("Male", "2005-11-28")
        self.assertEqual(t1, "Age is less than expected")

    def test_nation_success(self):
        t1 = validate_methods().eligibility_nation("Indian")
        self.assertEqual(t1, "success")

    def test_nation_invalid(self):
        t1 = validate_methods().eligibility_nation("Chinese")
        self.assertEqual(t1, "Nationality criteria not satisfied")

    def test_state_criteria_success(self):
        t1 = validate_methods().eligibility_state("Tamil Nadu")
        self.assertEqual(t1, "success")

    def test_state_criteria_invalid(self):
        t1 = validate_methods().eligibility_state("Chinese")
        self.assertEqual(t1, "State criteria not satisfied")

    def test_salary_criteria_success(self):
        t1 = validate_methods().eligibility_salary(20000)
        self.assertEqual(t1, "success")

    def test_salary_criteria_invalid(self):
        t1 = validate_methods().eligibility_salary(2000)
        self.assertEqual(t1, "Salary criteria not satisfied")

if __name__ == '__main__':
    unittest.main()
