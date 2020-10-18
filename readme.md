Two companies just merged. Your task is to add company B into company A database. 
The company B held their infromation in two files. company_employees and feedback_for_employees.

Their data was overlapping left and right:
company_employees had these fields (first_name, last_name, annual_salary, years_employed, email).
feedback_for_employees had (first_name, last_name, feedback, role, email).

Your main task is to comcatinate employees from 2 files into 1 record.

1.Use Employee class and class method to create new employee from a string.

2.Use context manager for database.

3.Lambda usage for filtering people with less than 3 years of work experience

4.Regular expressions usage for email check (can use staticmethod)

5.Serialization/Deserialization initial data is from json.

OUTPUT: Use already written get_employees method to show the comcatinated record