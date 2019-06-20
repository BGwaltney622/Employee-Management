import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Password123!",
    database = "employees"
)

mycursor = mydb.cursor()

sqlFormula = "INSERT INTO employees (name, ssn, phone, email, salary) VALUES (%s, %s, %s, %s, %s)"

mycursor.execute("SELECT COUNT(*) FROM employees")
row_count = mycursor.fetchone()[0]


#  Runs the program and allows the user to quit using the program
def run_program():
    while True:
        print('--------------------Employee Management System--------------------------')
        print('              There are (' + f'{row_count}' + ') employees in the system.')
        print('------------------------------------------------------------------------\n')
        print('1. Add new Employee')
        print('2. View all employees')
        print('3. Search employee by SSN')
        print('4. Edit employee information')
        print('5. Leave employee management system\n')
        print('------------------------------------------------------------------------\n')
        add = input('Please enter your option number: ')
        add = add.lower()
        if add == '1':
            add_employee()
        elif add == '2':
            view_employee()
        elif add == '3':
            search_employee()
        elif add == '4':
            edit_employee()
        elif add == '5':
            exit()
        else:
            print('Error! please enter a number 1-6')


# Creates the function which asks for employees
def add_employee():
    while True:
        name = str(input("Enter the Employees Full Name: "))
        ssn = str(input("Enter the Employees Full Social Security Number: "))
        phone = str(input("Enter the Employees Phone Number: "))
        email = str(input("Enter the Employees Email Address: "))
        salary = str(input("Enter the Employees Salary: "))

        employee = (name, ssn, phone, email, salary)
        mycursor.execute(sqlFormula, employee)
        mydb.commit()

        print(f'\nEmployee has been added to the database.')

        #  Allows the user to add another Employee
        while True:
            again = input('Do you want to add another employee? yes or no: ')
            again = again.lower()
            if again == 'yes':
                add_employee()
            elif again == 'no':
                run_program()
            else:
                print('Error! Please enter yes or no.')


#  Creates function that returns all employees
def view_employee():
    if row_count >= 1:
        mycursor.execute("SELECT * FROM employees")
        result = mycursor.fetchall()
        for employee in result:
            print(f'--------------{employee[0]}--------------')
            print(f'SSN: {employee[1]}')
            print(f'Phone: {employee[2]}')
            print(f'Email: {employee[3]}')
            print(f'Salary: ${employee[4]}')
            print('------------------------------------------')
    else:
        print('No Employees to view')


#  Creates the function which allows the user to search by SSN
def search_employee():
    employee_ssn = str(input('Enter the social security number of the employee you would like to view: '))
    try:
        if row_count >= 1:
            mycursor.execute("SELECT * FROM employees")
            result = mycursor.fetchall()
            for employee in result:
                if employee_ssn in employee:
                    print(f'--------------{employee[0]}--------------')
                    print(f'SSN: {employee[1]}')
                    print(f'Phone: {employee[2]}')
                    print(f'Email: {employee[3]}')
                    print(f'Salary: ${employee[4]}')
                    print('------------------------------------------')
        else:
            print('No Employees to view')

    except:
        print('Error!')


#  Creates the Function which allows the user to edit an employee
def edit_employee():
    employee_ssn = str(input('Enter the social security number of the employee you would like to edit: '))
    try:
        if row_count >= 1:
            mycursor.execute("SELECT * FROM employees")
            result = mycursor.fetchall()
            for employee in result:
                if employee_ssn in employee:
                    print(f'--------------{employee[0]}--------------')
                    print(f'SSN: {employee[1]}')
                    print(f'Phone: {employee[2]}')
                    print(f'Email: {employee[3]}')
                    print(f'Salary: ${employee[4]}')
                    print('------------------------------------------')
                while True:
                    edit = int(input('What information would you like to edit?\n'
                                     'Enter 1 for Full Name\n'
                                     'Enter 2 for SSN\n'
                                     'Enter 3 for Phone\n'
                                     'Enter 4 for Email\n'
                                     'Enter 5 for Salary\n'
                                     'Enter 6 to quit edit\n'
                                     'Please make a Selection 1-6: '))
                    if edit == 1:
                        name = str(input('Enter updated Full Name:'))
                        mycursor.execute("UPDATE employees SET name = %s WHERE ssn = %s", (name, employee_ssn))
                        mydb.commit()
                        break
                    elif edit == 2:
                        ssn = str(input('Enter updated SSN:'))
                        mycursor.execute("UPDATE employees SET ssn = %s WHERE ssn = %s", (ssn, employee_ssn))
                        mydb.commit()
                        break
                    elif edit == 3:
                        phone = str(input('Enter updated phone:'))
                        mycursor.execute("UPDATE employees SET phone = %s WHERE ssn = %s", (phone, employee_ssn))
                        mydb.commit()
                        break
                    elif edit == 4:
                        email = str(input('Enter updated Email:'))
                        mycursor.execute("UPDATE employees SET email = %s WHERE ssn = %s", (email, employee_ssn))
                        mydb.commit()
                        break
                    elif edit == 5:
                        salary = str(input('Enter updated salary:'))
                        mycursor.execute("UPDATE employees SET salary = %s WHERE ssn = %s", (salary, employee_ssn))
                        mydb.commit()
                        break
                    elif edit == 6:
                        run_program()
                    else:
                        print(f'{edit} is not a valid selection. Please select 1-6!')
    except:
        print('Error!')


run_program()