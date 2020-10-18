import re


class Employee():
    def __init__(self, first_name: str, last_name: str, role: str,
                 annual_salary: float, feedback: int,
                 years_employed: int, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.annual_salary = annual_salary
        self.feedback = feedback
        self.years_employed = years_employed
        self.email = email

    @classmethod
    def create_from_string(cls, employee_string: str):
        first_name, last_name, role, annual_salary, feedback, years_employed, email = employee_string.split(",")
        annual_salary, feedback, years_employed = float(annual_salary), int(feedback), int(years_employed)
        if cls.validate_email(email):
            return cls(first_name, last_name, role, annual_salary, feedback, years_employed, email)

    @staticmethod
    def validate_email(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            return True
        return False
