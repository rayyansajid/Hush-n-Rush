import CS21034_14 as file
import CS21034_16 as emp
class Administrator(file.User):
    def __init__(self):
        super().__init__()
        self.Prod = file.Products()
        self.truth_value = self.CheckInFile()
        file.Products.Give_Prod_Quantity_Dict()
        self.Employee=emp.Delivery_Employee()

    def CheckInFile(self, y='CS21034_9.txt'):
        '''This method checks the admin credentials'''
        with open(y, 'r') as f:
            File_Strg = f.read()
            if self.name in File_Strg and self.mail in File_Strg and self.password in File_Strg:
                return True
            return False

    def SaveToFile(self):
        '''This is an implementation of the abstract method of User class'''
        pass

    def View_Stock(self):
        '''This method allows the administrator to view the stock'''
        print()
        print('Your Remaining Stock is: ')
        for items in file.Products.Stock_Prod_Quantity_dict.items():
            print(f'{items[1]} {items[0]} are remaining.')

    @classmethod
    def notification(cls):
        '''This class method simply notifies if any product is less than 10'''
        print('NOTIFICATIONS')
        maximum = []
        for value in file.Products.Stock_Prod_Quantity_dict.values():
            maximum.append(value)
        if min(maximum) > 10:
            print('All items are well Stocked.')
        else:
            for item in file.Products.Stock_Prod_Quantity_dict.items():
                if item[1] <= 10:
                    print(f'Only {item[1]} {item[0]} are left ')

    def Remove_Stock(self):
        '''This method allows the admin to remove from stock '''
        self.View_Stock()
        while True:
            try:
                print()
                Prod_name = input(f'Which Product do you want to remove?\n'
                                  f'Enter Product name:')
                QuantityToBeRemoved = input(f'Enter number of {Prod_name} to be removed: ')
                if Prod_name=='' or QuantityToBeRemoved=='':
                    raise file.Ex.NoValue
                elif Prod_name.isdigit():
                    raise file.Ex.NumericError
                elif QuantityToBeRemoved.isalpha():
                    raise file.Ex.AlphabeticError
            except file.Ex.NoValue:
                print()
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                continue
            except file.Ex.NumericError:
                print()
                print('Enter Alphabets please')
                continue
            except file.Ex.AlphabeticError:
                print()
                print('Enter Number please')
                continue
            else:
                QuantityToBeRemoved=int(QuantityToBeRemoved)
                break
        f = file.Products.Stock_Prod_Quantity_dict[Prod_name]
        file.Products.Stock_Prod_Quantity_dict[Prod_name] = f - QuantityToBeRemoved
        print()
        print(f'{QuantityToBeRemoved} {Prod_name} is/are removed from stock')
        file.Products.reset_Quantity()

    def Feedback_Checker(self):
        '''This method allows the admin to check the feedback given by respected customers'''
        while True:
            try:
                print()
                choice = input('Which Feedback do you want to examine?\n'
                               'a)Good\n'
                               'b)Bad\n'
                               'Your Choice(a or b):')
                if choice == '':
                    raise file.Ex.NoValue
                elif choice.isdigit():
                    raise file.Ex.NumericError
                elif ord(choice) != 97 and ord(choice) != 65 and ord(choice) != 98 and ord(choice) != 66:
                    raise file.Ex.RangeError
            except file.Ex.NoValue:
                print()
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                continue
            except file.Ex.NumericError:
                print()
                print('Enter Alphabet please')
                continue
            except file.Ex.RangeError:
                print()
                print('Enter correct Alphabet (i.e. a or b)')
                continue
            else:
                break
        if choice == 'a' or choice == 'A':
            with open('CS21034_7.txt', 'r') as f:
                print('Good Feedbacks:\n' + '*' * 15)
                print(f.read())
        elif choice == 'b' or choice == 'B':
            with open('CS21034_8.txt', 'r') as f:
                print('Bad Feedbacks:\n' + '*' * 14)
                print(f.read())
        else:
            print()
            print('Invalid Choice')
            return

    def Add_Stock(self):
        '''This method allows the admin to add in the stock '''
        self.View_Stock()
        while True:
            try:
                print()
                Prod_name = input('Enter name of Product you want to add: ')
                QuantityToBeAdded = input(f'Enter number of {Prod_name} to be added: ')
                if Prod_name=='' or QuantityToBeAdded=='':
                    raise file.Ex.NoValue
                elif Prod_name.isdigit():
                    raise file.Ex.NumericError
                elif QuantityToBeAdded.isalpha():
                    raise file.Ex.AlphabeticError
            except file.Ex.NoValue:
                print()
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                continue
            except file.Ex.NumericError:
                print()
                print('Enter Alphabets please')
                continue
            except file.Ex.AlphabeticError:
                print()
                print('Enter Number please')
                continue
            else:
                QuantityToBeAdded=int(QuantityToBeAdded)
                break
        f = file.Products.Stock_Prod_Quantity_dict[Prod_name]
        file.Products.Stock_Prod_Quantity_dict[Prod_name] = f + QuantityToBeAdded
        print()
        print(f'{QuantityToBeAdded} {Prod_name} is/are added to stock')
        file.Products.reset_Quantity()

    def Manage_EmployeesForDelivery(self):
        '''This method Allows the admin to Execute certain operations related to Employees'''
        while True:
            while True:
                try:
                    Admin_Choice=input(f'Select an operation:\n'
                                        f'a) Show Employees\n'
                                        f'b) Send Bonus\n'
                                        f'c) Send Salary\n'
                                        f'Enter Your choice(a,b,c): ')
                    if Admin_Choice == '':
                        raise file.Ex.NoValue
                    elif Admin_Choice.isdigit():
                        raise file.Ex.NumericError
                    elif ord(Admin_Choice) != 97 and ord(Admin_Choice) != 65 and ord(Admin_Choice) != 98 and ord(Admin_Choice) != 66 and ord(Admin_Choice) != 99 and ord(Admin_Choice) != 67:
                        raise file.Ex.RangeError
                except file.Ex.NoValue:
                    print()
                    print('Empty text is not acceptable\n'
                          'Kindly Enter something')
                    continue
                except file.Ex.NumericError:
                    print()
                    print('Enter Alphabet please')
                    continue
                except file.Ex.RangeError:
                    print()
                    print('Enter correct Alphabet (i.e. a or b)')
                    continue
                else:
                    break

            if Admin_Choice=='a' or Admin_Choice=='A':
                print()
                self.Employee.ShowEmployees()
            elif Admin_Choice=='b' or Admin_Choice=='B':
                print()
                Up_Info=self.BonusOrSalaryToEmployees('Bonus')
                self.Employee.Write_UpdatedRecord(Up_Info,'CS21034_10.txt')
            elif Admin_Choice=='c' or Admin_Choice=='C':
                print()
                Up_Info=self.BonusOrSalaryToEmployees('Salary')
                self.Employee.Write_UpdatedRecord(Up_Info, 'CS21034_10.txt')
            else:
                print('Invalid Choice')
            while True:
                try:
                    print()
                    ch_1 = input('Do you want to continue managing Employees?\n'
                                 'Enter choice(Yes or No):')
                    if ch_1=='':
                        raise file.Ex.NoValue
                    elif ch_1.isdigit():
                        raise file.Ex.NumericError
                    elif ch_1!='Yes' and ch_1 != 'No' and ch_1 != 'yes' and ch_1!='no':
                        raise file.Ex.RangeError
                except file.Ex.NoValue:
                    print()
                    print('Empty text is not acceptable\n'
                          'Kindly Enter something')
                    continue
                except file.Ex.NumericError:
                    print()
                    print('Enter Alphabets please')
                    continue
                except file.Ex.RangeError:
                    print()
                    print('Enter correct Word (i.e. YEs or No)')
                    continue
                else:
                    break
            if ch_1 == 'Yes' or ch_1 == 'yes':
                continue
            elif ch_1 == 'No' or ch_1 == 'no':
                break

    def BonusOrSalaryToEmployees(self,TypeOfAmount):
        '''This method allows the admin to give bonus or salary to the employee'''
        Count_EmpOrd_Dict = self.Employee.ShowEmployees('SEND AMOUNT')
        while True:
            try:
                print()
                choice = input(f'Enter an employee number to send {TypeOfAmount}: ')
                if choice=='':
                    raise file.Ex.NoValue
                elif choice.isalpha():
                    raise file.Ex.AlphabeticError
            except file.Ex.NoValue:
                print()
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                continue
            except file.Ex.AlphabeticError:
                print()
                print('Please enter Number only')
            else:
                choice=int(choice)
                break
        EmpOrd_Lst = Count_EmpOrd_Dict[choice]
        UPDATED_LST=[]
        with open('CS21034_10.txt','r') as f:
            lines=f.readlines()
            for line in lines:
                if EmpOrd_Lst[1] in line:
                    line=line.strip()
                    self.Emp_detail_List=line.split(',')
                    if TypeOfAmount=='Salary':
                        self.Emp_detail_List[5]=str(eval(self.Emp_detail_List[5])+emp.Delivery_Employee.salary)+'\n'
                        print()
                        print(f'Monthly salary of PKR{emp.Delivery_Employee.salary} is sent to Mr.{self.Emp_detail_List[0]}')
                    elif TypeOfAmount=='Bonus':
                        Bonus=int(input('Enter Amount of Bonus: '))
                        self.Emp_detail_List[5]=str(eval(self.Emp_detail_List[5])+Bonus)
                        print()
                        print(f'A Bonus of PKR{Bonus} is sent to Mr.{self.Emp_detail_List[0]}')
                    UPDATED_LST.append(self.Emp_detail_List[0]+','+self.Emp_detail_List[1]+','
                                       +self.Emp_detail_List[2]+','+self.Emp_detail_List[3]
                                       +','+self.Emp_detail_List[4]+','+self.Emp_detail_List[5]+'\n')
                else:
                    UPDATED_LST.append(line)
            return UPDATED_LST

    def Manage_Stock(self):
        '''This method Allows the admin to Execute certain operations related to Stock'''
        while True:
            while True:
                try:
                    choice_2 = input(f'What do you want to do?\n'
                                     f'a)View Stock\n'
                                     f'b)Add Stock\n'
                                     f'c)Remove Stock\n'
                                     f'Enter Your Choice(a,b,c): ')
                    if choice_2 == '':
                        raise file.Ex.NoValue
                    elif choice_2.isdigit():
                        raise file.Ex.NumericError
                    elif ord(choice_2) != 97 and ord(choice_2) != 65 and ord(choice_2) != 98 and ord(choice_2) != 66 and ord(choice_2) != 99 and ord(choice_2) != 67:
                        raise file.Ex.RangeError
                except file.Ex.NoValue:
                    print()
                    print('Empty text is not acceptable\n'
                          'Kindly Enter something')
                    continue
                except file.Ex.NumericError:
                    print()
                    print('Enter Alphabet please')
                    continue
                except file.Ex.RangeError:
                    print()
                    print('Enter correct Alphabet (i.e. a or b)')
                    continue
                else:
                    break
            if choice_2 == 'a' or choice_2 == 'A':
                self.View_Stock()
            elif choice_2 == 'b' or choice_2 == 'B':
                self.Add_Stock()
            elif choice_2 == 'c' or choice_2 == 'C':
                self.Remove_Stock()
            else:
                print('Enter Valid choice')
            print()
            ch_1=input('Do you want to continue managing stock?\n'
                       'Enter choice(Yes or No):')
            if ch_1=='Yes' or ch_1=='yes':
                continue
            elif ch_1=='No' or ch_1=='no':
                break