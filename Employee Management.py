employee_bank = []


def add_employee():  # Creates the main function which asks for employees
    print('There are (' + str(len(employee_bank)) + ') employees in the system. ')
    while True:
        # Collects Employees name from User
        name = str(input("Enter the Employees Full Name: "))

        # Collects Employees social security number from User
        ssn = str(input("Enter the Employees Full Social Security Number: "))

        # Collects Employees phone number from User
        phone = str(input("Enter the Employees Phone Number: "))

        # Collects Employees email from User
        email = str(input("Enter the Employees Email Address: "))

        # Collects Employees salary from User
        salary = str(input("Enter the Employees Salary: "))

        employee = [name, ssn, phone, email, salary]
        employee_bank.append(employee)

        while True:
            again = input('Do you want to add another employee? yes or no: ')
            again = again.lower()
            if again == 'yes':
                add_employee()
            elif again == 'no':
                run_program()
            else:
                print('Error! Please enter yes or no.')


def view_employee():
    if len(employee_bank) >= 1:
        for employee in employee_bank:
            print(str(employee[0:])[1:-1])
    else:
        print('No Employees to view')


def run_program():
    while True:
        print('There are (' + str(len(employee_bank)) + ') employees in the system. ')
        add = input('Would you like to add an employee, view all employees, or quit? Enter add, view, or quit: ')
        add = add.lower()
        if add == 'add':
            add_employee()
        elif add == 'view':
            view_employee()
        elif add == 'quit':
            exit()
        else:
            print('Error! please enter add or view.')


run_program()