import sqlite3


class DatabaseContextManager(object):

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()


def create_employee_table():
    query = """CREATE TABLE Employees(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                role TEXT,
                annual_salary FLOAT,
                feedback INTEGER)"""
    with DatabaseContextManager("employees") as db:
        db.execute(query)


def create_employee(first_name: str, last_name: str, annual_salary: float):
    query = f"INSERT INTO Employees(first_name, last_name, annual_salary) VALUES('{first_name}','{last_name}',{annual_salary})"
    with DatabaseContextManager("employees") as db:
        db.execute(query)


def get_employee(first_name: str, last_name: str):
    query = f"SELECT * FROM Employees WHERE first_name = {first_name} OR last_name = {last_name}"
    with DatabaseContextManager("employees") as db:
        db.execute(query)


def update_employee_feedback(feedback: int, role: str, first_name: str, last_name: str):
    query = f"UPDATE Employees SET feedback = {feedback}, role = {role} WHERE first_name = {first_name} AND last_name = {last_name}"
    with DatabaseContextManager("employees") as db:
        db.execute(query)
