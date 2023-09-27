import CS21034_14 as f
import CS21034_6 as Ex
import CS21034_16 as Del
import CS21034_15 as Adm
print()
print('\t\t','_'*10,'HUSH & RUSH','_'*10)
print()
while True:
    while True:
        try:
            Choice=input('What is your Designation?\n'
                         'a) Customer\n'
                         'b) Administrator\n'
                         'c) Delivery Rider\n'
                         'Enter choice(a,b,c):')
            if Choice == '':
                raise Ex.NoValue
            elif Choice.isdigit():
                raise Ex.NumericError
            elif ord(Choice) != 97 and ord(Choice) != 65 and ord(Choice) != 98 and ord(
                    Choice) != 66 and ord(Choice) != 99 and ord(Choice) != 67:
                raise Ex.RangeError
        except Ex.NoValue:
            print('Empty text is not acceptable\n'
                  'Kindly Enter something')
            continue
        except Ex.NumericError:
            print('Enter Alphabet please')
            continue
        except Ex.RangeError:
            print('Enter correct Alphabet (i.e. a or b)')
            continue
        else:
            break
    if Choice=='a' or Choice=='A':
            print()
            print('\t\tWelcome Dear Customer Of HUSH & RUSH')
            cust=f.Customer()
            while True:
                while True:
                    try:
                        in1=input(f'What do you want to do?\n'
                          f'a)Shop Some interesting items\n'
                          f'b)See History of your Orders\n'
                          f'Enter Choice(a or b): ')
                        if in1 == '':
                            raise Ex.NoValue
                        elif in1.isdigit():
                            raise Ex.NumericError
                        elif ord(in1) != 97 and ord(in1) != 65 and ord(in1) != 98 and ord(
                                in1) != 66:
                            raise Ex.RangeError
                    except Ex.NoValue:
                        print('Empty text is not acceptable\n'
                              'Kindly Enter something')
                        continue
                    except Ex.NumericError:
                        print('Enter Alphabet please')
                        continue
                    except Ex.RangeError:
                        print('Enter correct Alphabet (i.e. a or b)')
                        continue
                    else:
                        break
                if in1=='a' or in1=='A':
                    print()
                    print('\t\tHERE ARE THE DOMAINS YOU CAN CHOOSE FROM')
                    cust.Show_Choose_And_Print()
                    while True:
                        while True:
                            try:
                                Decision=input(f'Do you want to:\n'
                                               f'a) See Cart\n'
                                               f'b) Add to cart\n'
                                               f'c) Remove from Cart\n'
                                               f'd) Proceed to Checkout\n'
                                               f'Your Choice(a,b,c,d): ')
                                if Decision == '':
                                    raise Ex.NoValue
                                elif Decision.isdigit():
                                    raise Ex.NumericError
                                elif ord(Decision) != 97 and ord(Decision) != 65 and ord(Decision) != 98 and ord(
                                        Decision) != 66 and ord(Decision) != 99 and ord(Decision) != 67 and ord(Decision) != 100 and ord(Decision) != 68:
                                    raise Ex.RangeError
                            except Ex.NoValue:
                                print('Empty text is not acceptable\n'
                                      'Kindly Enter something')
                                continue
                            except Ex.NumericError:
                                print('Enter Alphabet please')
                                continue
                            except Ex.RangeError:
                                print('Enter correct Alphabet (i.e. a or b)')
                                continue
                            else:
                                break
                        if Decision=='a' or Decision=='A':
                            cust.Show_Shopping_Cart()
                            continue
                        elif Decision=='b' or Decision=='B':
                            cust.Add_To_ShoppingCart()
                            continue
                        elif Decision=='c' or Decision=='C':
                            cust.Remove_From_ShoppingCart()
                            continue
                        elif Decision=='D' or Decision=='d':
                            cust.Final_Formalities()
                            break
                        else:
                            print('Invalid Input')
                            continue
                elif in1=='b' or in1=='B':
                    cust.History_Provider()
                customer_ch = input('What do you want to do?\n'
                                    'a) Continue in your ID\n'
                                    'b) LogOut\n'
                                    'Your Choice(a,b): ')
                if customer_ch == 'a' or customer_ch == 'A':
                    continue
                elif customer_ch == 'b' or customer_ch == 'B':
                    break
            print('Do you want to continue using the App?(y/n)',end='')
            inp=input()
            if inp=='Y' or inp=='y':
                continue
            elif inp=='N' or inp=='n':
                break
    elif Choice=='b'or Choice=='B':
        Admin=Adm.Administrator()
        if Admin.truth_value==True:
            print('\t\tWelcome Administrator of HUSH & RUSH')
            print()
            while True:
                while True:
                    try:
                        choice=input(f'Which Operation do you want to execute?\n'
                                        f'a) View Notification\n'
                                        f'b) View FeedBacks\n'
                                        f'c) Manage Stock\n'
                                        f'd) Manage Employees\n'
                                        f'Enter your Choice(a,b,c,d): ')
                        print()
                        if choice == '':
                            raise Ex.NoValue
                        elif choice.isdigit():
                            raise Ex.NumericError
                        elif ord(choice) != 97 and ord(choice) != 65 and ord(choice) != 98 and ord(
                                choice) != 66 and ord(choice) != 99 and ord(choice) != 67 and ord(choice) != 100 and ord(choice) != 68:
                            raise Ex.RangeError
                    except Ex.NoValue:
                        print('Empty text is not acceptable\n'
                              'Kindly Enter something')
                        continue
                    except Ex.NumericError:
                        print('Enter Alphabet please')
                        continue
                    except Ex.RangeError:
                        print('Enter correct Alphabet (i.e. a or b)')
                        continue
                    else:
                        break
                if choice=='a' or choice=='A':
                    Admin.notification()
                elif choice == 'b' or choice == 'B':
                    Admin.Feedback_Checker()
                elif choice=='c' or choice=='C':
                    Admin.Manage_Stock()
                elif choice=='d' or choice=='D':
                    Admin.Manage_EmployeesForDelivery()
                while True:
                    try:
                        print()
                        admin_ch=input('What do you want to do?\n'
                                       'a) Continue in your ID\n'
                                       'b) LogOut\n'
                                       'Your Choice(a,b): ')
                        print()
                        if admin_ch == '':
                            raise Ex.NoValue
                        elif admin_ch.isdigit():
                            raise Ex.NumericError
                        elif ord(admin_ch) != 97 and ord(admin_ch) != 65 and ord(admin_ch) != 98 and ord(
                                admin_ch) != 66:
                            raise Ex.RangeError
                    except Ex.NoValue:
                        print()
                        print('Empty text is not acceptable\n'
                              'Kindly Enter something')
                        continue
                    except Ex.NumericError:
                        print()
                        print('Enter Alphabet please')
                        continue
                    except Ex.RangeError:
                        print()
                        print('Enter correct Alphabet (i.e. a or b)')
                        continue
                    else:
                        break
                if admin_ch=='a' or admin_ch=='A':
                    continue
                elif admin_ch=='b' or admin_ch=='B':
                    break
        else:
            print('Enter Valid Credentials!')
        print('Do you want to continue using the App?(y/n)',end='')
        inp = input()
        if inp == 'Y' or inp == 'y':
            continue
        elif inp == 'N' or inp == 'n':
            break
    elif Choice=='c' or Choice=='C':
        Employee=Del.Delivery_Employee()
        Employee.Take_Info()
        while True:
            while True:
                try:
                    choice=input(f'What do you want to do?\n'
                                 f'a) Inspect Balance\n'
                                 f'b) See Orders to be Delivered\n'
                                 f'Enter Choice(a,b): ')
                    print()
                    if choice == '':
                        raise Ex.NoValue
                    elif choice.isdigit():
                        raise Ex.NumericError
                    elif ord(choice) != 97 and ord(choice) != 65 and ord(choice) != 98 and ord(
                            choice) != 66:
                        raise Ex.RangeError
                except Ex.NoValue:
                    print()
                    print('Empty text is not acceptable\n'
                          'Kindly Enter something')
                    continue
                except Ex.NumericError:
                    print()
                    print('Enter Alphabet please')
                    continue
                except Ex.RangeError:
                    print()
                    print('Enter correct Alphabet (i.e. a or b)')
                    continue
                else:
                    break
            if choice=='a' or choice=='A':
                Employee.Show_Balance()
                print()
            elif choice=='b' or choice=='B':
                Employee.Display_order()
                print()
            else:
                print('invalid choice')
            while True:
                try:
                    print()
                    ch_1 = input(f'What do you want to do?\n'
                                 f'a) Continue in your ID\n'
                                 f'b) Log Out\n'
                                 f'Enter choice(a or b):')
                    if ch_1 == '':
                        raise Ex.NoValue
                    elif ch_1.isdigit():
                        raise Ex.NumericError
                    elif ord(ch_1) != 97 and ord(ch_1) != 65 and ord(ch_1) != 98 and ord(
                            ch_1) != 66:
                        raise Ex.RangeError
                except Ex.NoValue:
                    print()
                    print('Empty text is not acceptable\n'
                          'Kindly Enter something')
                    continue
                except Ex.NumericError:
                    print()
                    print('Enter Alphabet please')
                    continue
                except Ex.RangeError:
                    print()
                    print('Enter correct Alphabet (i.e. a or b)')
                    continue
                else:
                    break
            if ch_1 == 'a' or ch_1 == 'A':
                continue
            elif ch_1 == 'b' or ch_1 == 'B':
                break
        print('Do you want to continue using the App?(y/n)',end='')
        inp = input()
        if inp == 'Y' or inp == 'y':
            continue
        elif inp == 'N' or inp == 'n':
            break
