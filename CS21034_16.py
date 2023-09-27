import CS21034_14 as files
class Delivery_Employee(files.User):
    salary = 25000
    comission_per_ord=150

    def __init__(self):
        pass

    def Take_Info(self):
        '''This method Simply takes the Employee details'''
        while True:
            super().__init__()
            self.truth_value = self.CheckInFile('CS21034_10.txt')
            if self.truth_value == True:
                with open('CS21034_10.txt','r') as f:
                    lines=f.readlines()
                    for line in lines:
                        if self.name in line and self.mail in line and self.password in line:
                            line=line.strip()
                            line_lst=line.split(',')
                            self.Phone_number =line_lst[3]
                            self.Acc_number=line_lst[4]
                            self.BankBal=line_lst[5]
                print('Your account is already present')
                return
            elif self.truth_value == False:
                self.Phone_number = input('Enter phone number please :(+92) ')
                self.Acc_number = input('Enter your account number please :')
                self.BankBal=input('Enter your bank Balance: ')
                self.SaveToFile()
                print()
                print('Your account has been created successfully')
                return
            elif self.truth_value == 'invalid':
                print()
                print('Enter correct password')

    def SaveToFile(self):
        '''This method writes the employee details in the file '''
        with open('CS21034_10.txt', 'a') as f:
            f.write(self.name+','+self.mail+','+self.password+','+self.Phone_number+','+self.Acc_number+','+self.BankBal+'\n')
        with open('CS21034_12.txt','a') as f:
            f.write(self.name+':'+self.mail+':'+'0'+'\n')

    def Display_order(self):
        '''This method simply displays the orders to be delivered and prints appropriate msg if there are no orders'''
        with open('CS21034_11.txt', 'r+') as f:
            print()
            Null_Checker = f.read()
            if Null_Checker == '':

                print(f'No Orders to show, yet :(')
            else:
                with open('CS21034_11.txt','r') as l:
                    Ord_count=1
                    line_Lst=l.readlines()
                    print(f'{len(line_Lst)} Order(s) have been placed by our respected customers: ')
                    for line in line_Lst:
                        line=eval(line)
                        print(f'{Ord_count}.\n{line[0]}')
                        Ord_count+=1
                    self.orders_delievered = len(line_Lst)
                    OrdersDelivered = input('Type "DONE" after Delivering All orders: ')
                    if OrdersDelivered == "DONE" or OrdersDelivered == "Done" or OrdersDelivered == "done":
                        with open('CS21034_11.txt','w') as k:
                            print()
                            print(f'{self.orders_delievered} orders delivered successfully ')
                        with open('CS21034_12.txt', 'r') as m:
                            lines=m.readlines()
                            update_lst=[]
                            for line in lines:
                                if self.name in line and self.mail in line:
                                    line=line.strip()
                                    line_lst=line.split(':')
                                    line_lst[2]=str(eval(line_lst[2])+self.orders_delievered)+'\n'
                                    update_lst.append(line_lst[0]+':'+line_lst[1]+':'+line_lst[2]+'\n')
                                else:
                                    update_lst.append(line)
                            self.Write_UpdatedRecord(update_lst,'CS21034_12.txt')
                        Comission=self.Comission_Setter()
                        Update_Lst=self.ComissionBalance_Adder(Comission)
                        self.Write_UpdatedRecord(Update_Lst,'CS21034_10.txt')

    def Comission_Setter(self):
        '''This method simply setts the Employee commission'''
        self.comission = self.orders_delievered * Delivery_Employee.comission_per_ord
        print()
        print(f'Comission of Mr.{self.name} is {self.comission},\n'
              f'Pkr{self.comission} is sent to your Account number {self.Acc_number}')
        return self.comission

    def ComissionBalance_Adder(self,Comission):
        '''This method simply adds the comission in the backbalance of employee'''
        with open('CS21034_10.txt','r+') as f:
            lines=f.readlines()
            Updated_RecordLst=[]
            strg=''
            for SingleEmployee in lines:
                if self.mail and self.Phone_number and self.Acc_number in SingleEmployee:
                    SingleEmployee=SingleEmployee.strip()
                    Emp_details=SingleEmployee.split(',')
                    Emp_details[5] = str(eval(Emp_details[5]) + Comission) + '\n'
                    for items in Emp_details:
                        if items!=Emp_details[5]:
                            strg+=items+','
                        else:
                            strg+=items
                    Updated_RecordLst.append(strg)
                else:
                    Updated_RecordLst.append(SingleEmployee)
            return Updated_RecordLst

    def Write_UpdatedRecord(self,UpdatedRecord,filename):
        '''This method simply updates the file by using the provided UpdatedRecord list in given filename'''
        with open(filename,'w') as f:
            for Record in UpdatedRecord:
                f.write(Record)

    def ShowEmployees(self,OrdersDelivered=None):
            '''This method simply Shows the Employees to the Admin accordiung to the given arguments'''
            count = 1
            Dict = {}
            if OrdersDelivered != None:
                with open('CS21034_12.txt') as f:
                    Emps = f.readlines()
                    print()
                    print(' ' * 10 + '%-9s%-14s%-s' % ('S.no', 'Name', 'Orders Delivered'))
                    for Single_Emp in Emps:
                        Single_Emp = Single_Emp.strip()
                        Emp_lst = Single_Emp.split(':')
                        print(' ' * 11 + '%-8i%-19s%s' % (count, Emp_lst[0], Emp_lst[2]))
                        Dict[count] = [Emp_lst[0],Emp_lst[1],Emp_lst[2]]
                        count += 1
            elif OrdersDelivered == None:
                with open('CS21034_10.txt','r') as f:
                    All_Emps=f.readlines()
                    for line in All_Emps:
                        line=line.strip()
                        line_lst=line.split(',')
                        print(f'{count}. Mr.{line_lst[0]}')
                        Dict[count] = line_lst[0]
                        count+=1
            return Dict

    def Show_Balance(self):
        '''This method simply show the Employee his total bank balance'''
        with open('CS21034_10.txt','r') as f:
            lines=f.readlines()
            for line in lines:
                if self.mail and self.Phone_number and self.Acc_number in line:
                    line=line.strip()
                    Detail_lst=line.split(',')
                    print(f'Mr.{self.name}, your Bank balance is {Detail_lst[5]}')