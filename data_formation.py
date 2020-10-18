import json
from database import *
from employee import Employee


def concatinate_employee_data():
    """
    Function that goes through 2 files, parses data and saves it into list of objects.
    Benefits of this way is that we get a list of objects at the end.
    So we can manipulate data how we see fit for every object
    :return:
    """
    employee_object_list = []
    with open("company_employees.json", mode='r') as file:
        data = json.load(file)
        for company_employee in data['Employees']:
            employee_object_list.append(Employee(company_employee['firstName'], company_employee['lastName'], None,
                                                 company_employee['annual_salary'], None,
                                                 company_employee['years_employed'], company_employee['emailAddress']))

    with open("feedback_for_employees.json", mode='r') as feedback_file:
        data = json.load(feedback_file)

        for employee_feedback in data["Feedback"]:
            for employee in employee_object_list:
                if employee.email == employee_feedback["emailAddress"]:
                    employee.role = employee_feedback["role"]
                    employee.feedback = employee_feedback["feedback"]
                    break

    for employee_object in employee_object_list:
        if not check_if_employee_exists_in_database(employee_object.email):
            create_employee(employee_object.first_name, employee_object.last_name, employee_object.role,
                            employee_object.annual_salary, employee_object.feedback, employee_object.years_employed,
                            employee_object.email)


create_employee_table()
concatinate_employee_data()
get_employees()
