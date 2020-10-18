import json
from database import *


def concatinate_employee_data():
    """
    Function that goes through 2 files, parses data and saves it into list.
    Goes through both lists comparing each record and adds it into database.
    :return:
    """

    employee_list = []
    with open("company_employees.json", mode='r') as file:
        data = json.load(file)
        employee_list.append(data["Employees"])

    feedback_list = []
    with open("feedback_for_employees.json", mode='r') as feedback_file:
        data = json.load(feedback_file)
        feedback_list.append(data["Feedback"])

    for employee in employee_list[0]:
        for employee_feedback in feedback_list[0]:
            if employee["emailAddress"] == employee_feedback["emailAddress"]:
                if not check_if_employee_exists_in_database(employee['emailAddress']):
                    create_employee(employee['firstName'], employee['lastName'],
                                    employee_feedback['role'], employee['annual_salary'],
                                    employee_feedback['feedback'], employee['years_employed'],
                                    employee['emailAddress'])


create_employee_table()
concatinate_employee_data()
get_employees()
