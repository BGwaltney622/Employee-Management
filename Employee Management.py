#  Creates employee bank
employee_bank = []


#  Creates a clear function
def cls():
    print('\n' * 4)


#  Runs the program and allows the user to quit using the program
def run_program():
    while True:
        print('--------------------Employee Management System--------------------------')
        print('              There are (' + str(len(employee_bank)) + ') employees in the system.')
        print('------------------------------------------------------------------------\n')
        print('1. Add new Employee')
        print('2. View all employees')
        print('3. Search employee by SSN')
        print('4. Edit employee information')
        print('5. Export employees\' information into a text file')
        print('6. Import employees\' information from a text file')
        print('7. Leave employee management system\n')
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
            export_employee()
        elif add == '6':
            import_employee()
        elif add == '7':
            exit()
        else:
            print('Error! please enter a number 1-7')
            cls()


# Creates the function which asks for employees
def add_employee():
    print('There are (' + str(len(employee_bank)) + ') employees in the system. ')
    while True:
        name = str(input("Enter the Employees Full Name: "))
        ssn = str(input("Enter the Employees Full Social Security Number: "))
        phone = str(input("Enter the Employees Phone Number: "))
        email = str(input("Enter the Employees Email Address: "))
        salary = str(input("Enter the Employees Salary: "))

        employee = [name, ssn, phone, email, salary]
        employee_bank.append(employee)

        print(f'\nEmployee has been added to the database.')

        #  Allows the user to add another Employee
        cls()
        while True:
            again = input('Do you want to add another employee? yes or no: ')
            again = again.lower()
            if again == 'yes':
                add_employee()
            elif again == 'no':
                cls()
                run_program()
            else:
                print('Error! Please enter yes or no.')


#  Creates function that returns all employees
def view_employee():
    if len(employee_bank) >= 1:
        for employee in employee_bank:
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
        for employee in employee_bank:
            if employee_ssn in employee:
                print(f'--------------{employee[0]}--------------')
                print(f'SSN: {employee[1]}')
                print(f'Phone: {employee[2]}')
                print(f'Email: {employee[3]}')
                print(f'Salary: ${employee[4]}')
                print('------------------------------------------')
    except:
        print('Error!')


#  Creates the Function which allows the user to edit an employee
def edit_employee():
    employee_ssn = str(input('Enter the social security number of the employee you would like to edit: '))
    try:
        for employee in employee_bank:
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
                        employee[0]= name
                        break
                    elif edit == 2:
                        ssn = str(input('Enter updated SSN:'))
                        employee[1] = ssn
                        break
                    elif edit == 3:
                        phone = str(input('Enter updated phone:'))
                        employee[2] = phone
                        break
                    elif edit == 4:
                        email = str(input('Enter updated Email:'))
                        employee[3] = email
                        break
                    elif edit == 5:
                        salary = str(input('Enter updated salary:'))
                        employee[4] = salary
                        break
                    elif edit == 6:
                        run_program()
                    else:
                        print(f'{edit} is not a valid selection. Please select 1-6!')
    except:
        print('Error!')


#  Creates a function allowing the user to export the employee bank to a .txt
def export_employee():
    with open('Employee Database.txt', 'w+') as db:
        for employee in employee_bank:
            db.write(f'{employee[0]}, {employee[1]}, {employee[2]}, {employee[3]}, {employee[4]}\n')


#  Creates a function that allows the user to import from a .txt file
def import_employee():
    with open('Employee Database.txt', 'r') as db:
        contents = db.readlines()
        imported_employee = [x.split(', ') for x in contents]
        clean_employee = [[s.rstrip() for s in nested] for nested in imported_employee]
        for employee in clean_employee:
            employee_bank.append(employee)


run_program()
