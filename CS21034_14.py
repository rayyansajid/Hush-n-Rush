from abc import ABC, abstractmethod
from datetime import date
import CS21034_6 as Ex

class User(ABC):
    def __init__(self):
        while True:
            try:
                print()
                self.name = input('Enter name: ')
                self.mail = input('Enter email: ')
                self.password = input('Enter password: ')
                print()
                if self.name=='' or self.mail=='' or self.password=='':
                    raise Ex.NoValue
            except Ex.NoValue:
                print()
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                continue
            else:
                break

    @abstractmethod
    def SaveToFile(self):
        '''This is an Abstract method, All inheriting classes have to redefine it'''
        pass

    def CheckInFile(self, y):
        '''This method checks if user has entered valid credentials or not'''
        with open(y, 'r') as k:
            lines = k.readlines()
            for record in lines:
                if self.mail in record and self.password in record:
                    return True
                elif self.mail in record and self.password not in record:
                    return 'invalid'
                else:
                    return False

class Customer(User):
    def __init__(self):
        self.Cart = ShoppingCart()
        while True:
            super().__init__()
            self.truth_value = super().CheckInFile('CS21034_1.txt')
            if self.truth_value == True:
                print('Your account is already present\n')
                self.Take_Address()
                break
            elif self.truth_value == False:
                self.SaveToFile()
                print('Your account has been created successfully')
                self.Take_Address()
                break
            elif self.truth_value == 'invalid':
                print('Enter correct password')

    def SaveToFile(self):
        '''This method implements the abstract method in Parent class User,
        Saves the Details of Customer in the File in the required Format'''
        with open('CS21034_1.txt', 'a') as f:
            f.write(self.name + ',' + self.mail + ',' + self.password + '\n')

    def Take_Address(self):
        '''This method Takes the Address of customer and handle exceptions simultaneously'''
        while True:
            try:
                self.Address = input('Enter your Address: ')
                print()
                if self.Address == '':
                    raise Ex.NoValue
            except Ex.NoValue:
                print()
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                continue
            else:
                break

    def Show_Choose_And_Print(self):
        '''This method Calls the methods of Composed Class to Execute the required operations'''
        self.Cart.Show_Items()
        self.Cart.Choose_Domain()

    def Show_Shopping_Cart(self):
        '''This method calls the method from its composed class namely Shopping_Cart to show the items of cart to the customer'''
        self.Cart.Show_Cart()

    def Add_To_ShoppingCart(self):
        '''This method simply allows the customer to add items from different domains in the shopping cart'''
        Additional_Items={}
        Prod_Pr_dic={}
        Chose_Product_Dict={}
        Products.Give_Domain_Products_Dict(Products.Domain_Products_Dict)
        s_no=1
        print()
        print('\t\tHERE ARE THE DOMAINS YOU CAN CHOOSE FROM')
        print()
        for Domain in Products.Domain_Products_Dict:
            print(f'{s_no}. {Domain}')
            s_no+=1
        while True:
            try:
                domain_choice=input('Enter no. of domain you want to add products from: ')
                if domain_choice=='':
                    raise Ex.NoValue
                elif domain_choice.isalpha():
                    raise Ex.AlphabeticError
                elif not 49<=ord(domain_choice)<=52:
                    raise Ex.RangeError
            except Ex.NoValue:
                print()
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                continue
            except Ex.AlphabeticError:
                print()
                print('Enter a number please')

                continue
            except Ex.RangeError:
                print()
                print('Enter Correct number from the given domains please')

                continue
            else:
                break
        if domain_choice == '1':
            dom_prods=Products.Domain_Products_Dict['Clothing']
            self.AddCart_Supporter(dom_prods, Prod_Pr_dic, Chose_Product_Dict, Additional_Items)
        elif domain_choice=='2':
            dom_prods=Products.Domain_Products_Dict['Electronics']
            self.AddCart_Supporter(dom_prods, Prod_Pr_dic, Chose_Product_Dict, Additional_Items)
        elif domain_choice=='3':
            dom_prods=Products.Domain_Products_Dict['Grocery']
            self.AddCart_Supporter(dom_prods, Prod_Pr_dic, Chose_Product_Dict, Additional_Items)
        elif domain_choice=='4':
            dom_prods=Products.Domain_Products_Dict['Fruits']
            self.AddCart_Supporter(dom_prods, Prod_Pr_dic, Chose_Product_Dict, Additional_Items)
        else:
            print()
            print(f'Enter Valid Choice')

    def AddCart_Supporter(self,dom_prods,Prod_Pr_dic,Chose_Product_Dict,Additional_Items):
        '''This method simply allows the customer to add items from a single domain in the shopping cart'''
        count = 1
        countt = 1
        print()
        print('               %-15s%-17s%-13s' % ('S.no.', 'Product', 'Price'))
        for Prod_Price_Lst in dom_prods:
            print('                %-14s%-17s%-15s' % (str(count) + '.', Prod_Price_Lst[0], Prod_Price_Lst[1] + '/-'))
            count += 1
            Prod_Pr_dic[Prod_Price_Lst[0]] = eval(Prod_Price_Lst[1])
        for Product in Prod_Pr_dic:
            Chose_Product_Dict[countt] = Product
            countt += 1
        while True:
            while True:
                try:
                    print()
                    Pr_Choice = input(f'Enter Product number you want to add in cart: ')
                    if Pr_Choice=='':
                        raise Ex.NoValue
                    elif Pr_Choice.isalpha():
                        raise Ex.AlphabeticError
                    elif not 1<=int(Pr_Choice)<=10:
                        raise Ex.RangeError
                except Ex.AlphabeticError:
                    print()
                    print('Enter a number please')
                    continue
                except Ex.NoValue:
                    print()
                    print('Empty text is not acceptable\n'
                          'Kindly Enter something')
                    continue
                except Ex.RangeError:
                    print()
                    print('Enter correct number')
                    continue
                else:
                    Pr_Choice=int(Pr_Choice)
                    break
            Prod = Chose_Product_Dict[Pr_Choice]
            while True:
                try:
                    Quant = input(f'Enter Quantity of {Prod} to be added: ')
                    if Quant=='':
                        raise Ex.NoValue
                    elif Quant.isalpha():
                        raise Ex.AlphabeticError
                except Ex.AlphabeticError:
                    print()
                    print('Enter a number please')
                    continue
                except Ex.NoValue:
                    print()
                    print('Empty text is not acceptable\n'
                          'Kindly Enter something')
                    continue
                else:
                    Quant=int(Quant)
                    break
            Additional_Items[Prod] = Quant
            while True:
                try:
                    print()
                    decide = input('Do you want to continue Shopping(y/n): ')
                    if decide=='':
                        raise Ex.NoValue
                    elif decide.isdigit():
                        raise Ex.NumericError
                    elif ord(decide)!=121 and ord(decide)!=110 and ord(decide)!=89 and ord(decide)!=78:
                        raise Ex.RangeError
                except Ex.NumericError:
                    print()
                    print('Enter an Alphabet plz')
                    continue
                except Ex.RangeError:
                    print()
                    print('Enter correct Alphabet (i.e. Y or N)')
                    continue
                except Ex.NoValue:
                    print()
                    print('Empty text is not acceptable\n'
                          'Kindly Enter something')
                    continue
                else:
                    break
            if decide == 'y' or decide == 'Y':
                continue
            elif decide == 'N' or decide == 'n':
                self.Cart.Product_Quantity=Order.Give_Cart_Dict()
                self.Cart.Product_Quantity.update(Additional_Items)
                self.Cart.Write_CustomerChosenProduct_Quantity_Dict_InFile()
                break

    def Remove_From_ShoppingCart(self):
            '''This method calls the method of class Shopping cart to allow the Customer to Remove products from cart'''
            self.Cart.Remove_from_Cart()

    def Final_Formalities(self):
        '''This method Allows the customer to pay the Total amount and send feedback accordingly'''
        self.Cart.FinalOrderAndFeedback(self.name, self.mail, self.Address)

    def History_Provider(self):
        '''This method Allows the user to Check his previous placed orders'''
        with open('CS21034_2.txt','r') as f:
            print()
            print(f'Mr/Ms {self.name}, Your Order History is shown Below:')
            lines=f.readlines()
            for line in lines:
                line=eval(line)
                if self.mail in line[0]:
                    print(line[0])

class ShoppingCart:
    def __init__(self):
        self.Product_Quantity = {}
        self.Order = Order()

    def choose_Product(self):
        '''This method Allows the Customer to Choose the desired product from a specific domain '''
        while True:
            try:
                print()
                ask_user = int(input('Enter which product number do you want to choose: '))
                if ask_user in Products.Choose_Prod_Dict:
                    final_product = Products.Choose_Prod_Dict[ask_user]
                    print('Enter the quantity of', final_product, ':', end='')
                    choosee = int(input())
                    self.Product_Quantity[final_product] = choosee
                    print()
                    print('Do you want to continue shopping?(y/n) ', end='')
                    choice = input()
                    if choice == 'y' or choice == 'Y':
                        continue
                    elif choice == 'n' or choice == 'N':
                        self.Write_CustomerChosenProduct_Quantity_Dict_InFile()
                        print()
                        break
                else:
                    print('Please enter valid choice')
            except:
                print(f'Please enter integer')
    def Show_Cart(self):
        '''This method Allows the Customer to See The products/items from his cart '''
        count = 1
        print()
        print('Item(s) Included in your cart are: ')
        with open ('CS21034_3.txt','r') as f:
            items_in_cart=eval(f.read())
            for items in items_in_cart.items():
                print(f'{count}. {items[1]} {str(items[0])}(s)')
                count+=1
            print()

    def Remove_from_Cart(self):
        '''This user allows the customer to remove the undesired items from his cart'''
        self.Show_Cart()
        while True:
            try:
                ProdName = input('Enter name of product to be removed: ')
                if ProdName=='':
                    raise Ex.NoValue
                elif ProdName.isdigit():
                    raise Ex.NumericError
                for letter in ProdName:
                    if not letter.isalpha():
                        raise Ex.NumericError
            except Ex.NoValue:
                print()
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                continue
            except Ex.NumericError:
                print()
                print('Enter Alphabets only')
            else:
                break
        while True:
            try:
                print()
                QuantityToBeRemoved = input(f'Enter Quantity of {ProdName} to be removed,\n'
                                    f'Type All to completely remove {ProdName}: ')
                if QuantityToBeRemoved=='':
                    raise Ex.NoValue
                for i in QuantityToBeRemoved:
                    if not i.isdigit():
                        if ord(i)!=97 and ord(i)!=108 and ord(i)!=65 and ord(i)!=76 :
                            raise Ex.RangeError
            except Ex.NoValue:
                print()
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                continue
            except Ex.RangeError:
                print()
                print('Enter Correct Letters')
                continue
            else:
                break
        if QuantityToBeRemoved == 'All' or QuantityToBeRemoved == 'all' or QuantityToBeRemoved == 'ALL' or QuantityToBeRemoved == 'all':
            self.Product_Quantity=Order.Give_Cart_Dict()
            QuantityOfRemovedItems=self.Product_Quantity[ProdName]
            Removeditems = self.Product_Quantity.pop(ProdName)
            print()
            print(f'{Removeditems} {ProdName} is/are removed from your cart')
            print()
            self.Write_CustomerChosenProduct_Quantity_Dict_InFile()
            self.Order.UpdateStock('Remove from Cart',ProdName,QuantityOfRemovedItems)
        elif QuantityToBeRemoved.isdigit():
            OriginalChosenQuantity=self.Product_Quantity[ProdName]
            self.Product_Quantity[ProdName]=OriginalChosenQuantity-int(QuantityToBeRemoved)
            self.Write_CustomerChosenProduct_Quantity_Dict_InFile()
            self.Order.UpdateStock('Remove from Cart',ProdName,int(QuantityToBeRemoved))

    def Choose_Domain(self):
        '''This method allows the user to select a specific domain from which he/she wants to purchase products from'''
        count = 1
        countt = 1
        while True:
            try:
                choice = input('Enter the number of domain you want to choose products from :')
                if choice == '':
                    raise Ex.NoValue
                elif choice.isalpha():
                    raise Ex.AlphabeticError
                elif not 49<=ord(choice)<=52:
                    raise Ex.RangeError
            except Ex.NoValue:
                print()
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                print()
                continue
            except Ex.AlphabeticError:
                print()
                print('Enter a number please')
                print()
                continue
            except Ex.RangeError:
                print()
                print('Enter Correct number from the given domains please')
                continue
            else:
                choice=int(choice)
                break
        if choice in Products.Choose_Domain_Dict:
            final = Products.Choose_Domain_Dict[choice]
            display_prod = Products.Domain_Products_Dict[final]
            print()
            print('               %-15s%-17s%-13s' % ('S.no.', 'Product', 'Price'))
            for Pair_Product in display_prod:
                print('                %-14s%-17s%-15s' % (str(count) + '.', Pair_Product[0], Pair_Product[1] + '/-'))
                count += 1
                Products.Prod_Price_dict[Pair_Product[0]] = eval(Pair_Product[1])
            for Product in Products.Prod_Price_dict:
                Products.Choose_Prod_Dict[countt] = Product
                countt += 1
            ShoppingCart.choose_Product(self)
        else:
            print()
            print('Invalid input')

    def Show_Items(self):
        '''This method simply calls the method of Order class to show different domains to the customer'''
        self.Order.From_Product()

    def FinalOrderAndFeedback(self, name, email, Address):
        '''This method simply calls the method of order class to print the checkout slip and asks Customer for the feedback accordingly'''
        self.Order.Checkout_Slip(name, email, Address)
        self.Order.takefeedback()

    def Write_CustomerChosenProduct_Quantity_Dict_InFile(self):
        '''This method simply writes the customer's cart items along with their quantity in the file'''
        with open('CS21034_3.txt', 'w') as f:
            f.write(str(self.Product_Quantity))

class Order:
    def __init__(self):
        self.prod = Products()
        self.prod.Give_Prod_Quantity_Dict()
        self.shipping = Shipping_Details()
        self.prod.Final_ProductPriceDict_maker()

    def __str__(self):
        count = 1
        self.strg_ord += ' '*15+'%-9s%-15s%-13s%-16s%s' % ('Sno.', 'Product', 'Price', 'Quantity', 'Amount\n')
        self.Amount_list = []
        shopping_dict=Order.Give_Cart_Dict()
        for item in shopping_dict:
            self.strg_ord += ' '*16+'%-8s%-15s%-16s%-13s%s' % (
                str(count) + '.', item, str(Products.All_Product_Prices_Dict[item]) + '/-', str(shopping_dict[item]),
                str(Products.All_Product_Prices_Dict[item] * shopping_dict[item]) + '\n')
            self.Amount_list.append(shopping_dict[item] * Products.All_Product_Prices_Dict[item])
            count += 1
        self.strg_ord += self.Cal_total_payment()
        return self.strg_ord

    def Customer_Details_Stringer(self, name, email, Address):
        '''this method simply returns a part of checkout slip in which name,email and address of customer along with date is specified '''
        self.today = date.today()
        self.Date = self.today.strftime("%B %d, %Y")
        Details = ''
        Details += f'Date: {str(self.Date)}\n'
        Details += f'Name: {name}\nEmail: {email}\nAddress: {Address}\n'
        return Details

    def Checkout_Slip(self, name, email, Address):
        '''this method simply prints the Final Checkout Slip, writes it in files and asks the Customer the mode of payment'''
        user_Details = self.Customer_Details_Stringer(name, email, Address) + self.shipping.ConfirmationMail(email)
        self.strg_ord = ''
        self.strg_ord += user_Details
        print()
        print(self)
        self.Payment = Payment()
        if self.Payment.Pay == 'a' or self.Payment.Pay == 'A':
            self.Payment.Cash_On_Delivery(Address)
        else:
            self.Payment.Online_Payment()
        self.SlipInFile()
        self.UpdateStock('Add to Cart')

    def SlipInFile(self):
        '''This method simply writes the final Checkout slip in two files, one for Customer's own history and other for the delivery rider to deliver it'''
        self.Write_In_File('CS21034_2.txt')
        self.Write_In_File('CS21034_11.txt')

    def Write_In_File(self,filename):
        ''' this method simply appends the string to final Checkout slip to a list and write that list in provided filename'''
        with open(filename, 'a') as f:
            self.ListOfOrder = []
            self.ListOfOrder.append(self.strg_ord)
            f.write(str(self.ListOfOrder) + '\n')

    def Cal_total_payment(self):
        '''This method simply Calculates the Final Payment of Customer and returns a string of it'''
        self.summ_list = sum(self.Amount_list)
        string = 'Total Payment is :' + str(self.summ_list) + 'Rs\nTHANK YOU FOR SHOPPING!!\n'
        return string

    def takefeedback(self):
        '''This method simply Allows the user to Give feedback'''
        print()
        print(f'Do you want to give any feedback ?')
        while True:
            try:
                about_feedback = input(f'Your choice (Y) or (N):')
                print()
                if about_feedback == '':
                    raise Ex.NoValue
                elif about_feedback.isdigit():
                    raise Ex.NumericError
                elif ord(about_feedback) != 121 and ord(about_feedback) != 110 and ord(about_feedback) != 89 and ord(about_feedback) != 78:
                    raise Ex.RangeError
            except Ex.NumericError:
                print()
                print('Enter an Alphabet plz')
                continue
            except Ex.RangeError:
                print()
                print('Enter correct Alphabet (i.e. Y or N)')
                continue
            except Ex.NoValue:
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                continue
            else:
                break
        if about_feedback == 'y' or about_feedback == 'Y':
            while True:
                try:
                    print()
                    feedbackchoice = input(f'a)Did you have a good experience?(a)\n'
                                           f'b)Did you have a bad experience?(b)\n'
                                           f'Your choice(a,b): ')
                    if feedbackchoice=='':
                        raise Ex.NoValue
                    elif feedbackchoice.isdigit():
                        raise Ex.NumericError
                    elif ord(feedbackchoice)!=97 and ord(feedbackchoice)!=65 and ord(feedbackchoice)!=98 and ord(feedbackchoice)!=66:
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
            if feedbackchoice == 'a' or feedbackchoice=='A':
                Order.Write_Feedback('CS21034_7.txt')
            elif feedbackchoice == 'b' or feedbackchoice=='B':
                Order.Write_Feedback('CS21034_8.txt')
        elif about_feedback == 'N' or about_feedback == 'n':
            return
        else:
            print('Invalid Input')
            return

    @staticmethod
    def Write_Feedback(filename):
        '''This static method simply writes customer's feedback into file accordingly'''
        while True:
            try:
                print()
                feedback = input('Your feedback: ')
                if feedback=='':
                    raise Ex.NoValue
            except Ex.NoValue:
                print()
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                continue
            else:
                break
        with open(filename, 'a+') as f:
            f.write(feedback + '\n')
        print()
        print('Thank you for your feedback')
        print()

    def UpdateStock(self, Purpose='Add to Cart',Prod=None,Quantity=None):
        '''This method simply updates the Stock  i.e. removes or adds in the stock'''
        if Purpose=='Add to Cart' and Prod==None and Quantity==None:
            Cust_Dict = Order.Give_Cart_Dict()
            for Prod_s in Cust_Dict:
                Sold_Quantity = Cust_Dict[Prod_s]
                Stock_Quantity = Products.Stock_Prod_Quantity_dict[Prod_s]
                Products.Stock_Prod_Quantity_dict[Prod_s] = Stock_Quantity - Sold_Quantity
        else:
            Stock_Quantity=Products.Stock_Prod_Quantity_dict[Prod]
            Products.Stock_Prod_Quantity_dict[Prod] = Stock_Quantity + int(Quantity)
        self.prod.reset_Quantity()

    @classmethod
    def Give_Cart_Dict(cls):
        '''This static method simply returns the dictionary which consists of Customer's cart along with their quantity'''
        with open('CS21034_3.txt', 'r') as f:
            Cust_Dict = eval(f.read())
            return Cust_Dict

    def From_Product(self):
        '''This method simply calls the metod from Product class to show domains to Customer'''
        self.prod.Show_Domain()

class Products:
    Domain_Products_Dict = {}
    Prod_Price_dict = {}
    Choose_Prod_Dict = {}
    Choose_Domain_Dict = {}
    Stock_Prod_Quantity_dict = {}
    All_Product_Prices_Dict={}

    def Show_Domain(self):
        '''This method Shows Domains to the Customer'''
        S_no = 1
        Dict = Products.Give_Domain_Products_Dict(Products.Domain_Products_Dict)
        print()
        for Domains in Dict:
            print(str(S_no) + ') ' + Domains)
            Products.Choose_Domain_Dict[S_no] = Domains
            S_no += 1

    @staticmethod
    def Give_Domain_Products_Dict(dic):
        '''This static method returns the dictionary consisting of Domains and All the products of that domain in a list
        in the format :    {'DOMAIN_1':[[Product_1,Price]...],...}'''
        Item_List = []
        with open('CS21034_4.txt', 'r+') as P:
            lines = P.readlines()
            for line in lines:
                line = line.strip('\n')
                Domain_Product_List = line.split(';')
                dic[Domain_Product_List[0]] = Domain_Product_List[1]
            for Item in dic.items():
                Product_Price = Item[1].split(',')
                for Procut_Price_string in Product_Price:
                    ItemAndPrice = Procut_Price_string.split(':')
                    Item_List.append(ItemAndPrice)
                    dic[Item[0]] = Item_List
                Item_List = []
        return dic

    @classmethod
    def Give_Prod_Quantity_Dict(cls):
        '''This class method simply returns a dictionary consists of products along with their quantity present in the stock'''
        with open('CS21034_5.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                linep = line.strip()
                lineps = linep.split(':')
                Products.Stock_Prod_Quantity_dict[lineps[0]] = eval(lineps[1])
            return Products.Stock_Prod_Quantity_dict

    @classmethod
    def reset_Quantity(cls):
        '''This class method Simply updates the stock products and their quantity in the specified format'''
        with open('CS21034_5.txt', 'w') as f:
            for item in Products.Stock_Prod_Quantity_dict.items():
                strg = str(item[0]) + ':' + str(item[1]) + '\n'
                f.write(strg)

    @classmethod
    def Final_ProductPriceDict_maker(cls):
        '''This class method simply updates the class dictionary according to Products and their prices '''
        with open('CS21034_4.txt','r') as f:
            Products.Give_Domain_Products_Dict(Products.Domain_Products_Dict)
            for Domains  in Products.Domain_Products_Dict:
                Prod_TwoDimensionLst=Products.Domain_Products_Dict[Domains]
                for Pro_Price in Prod_TwoDimensionLst:
                    Products.All_Product_Prices_Dict[Pro_Price[0]]=eval(Pro_Price[1])

class Shipping_Details:
    def ConfirmationMail(self, email):
        '''This method simply return the comfirmatory string of order placed by customer'''
        return f'Following order is confirmed for email {email}\n'

class Payment:
    def __init__(self):
        while True:
            try:
                print()
                self.Pay = input(f'Enter mode of Payment:\n'
                                 f'a)Cash on Deivery\n'
                                 f'b)Online Payment\n'
                                 f'Enter Choice(a or b): ')
                if self.Pay == '':
                    raise Ex.NoValue
                elif self.Pay.isdigit():
                    raise Ex.NumericError
                elif ord(self.Pay) != 97 and ord(self.Pay) != 65 and ord(self.Pay) != 98 and ord(
                        self.Pay) != 66:
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
    def Cash_On_Delivery(self, address):
        '''This method simply returns the confirmatory string to deliver on Customer's address'''
        print()
        print(f'Cash on delivery is selected,\nAbove order will be delivered at {address}')

    def Online_Payment(self):
        '''This method simply allows the Customer to select the mode of online payment'''
        while True:
            try:
                print()
                credit_choice = input('How would you like to pay?\n'
                                      'a) On Credict Card\n'
                                      'b) Through EasyPaisa\n'
                                      'Your Choice(a,b): ')
                if credit_choice == '':
                    raise Ex.NoValue
                elif credit_choice.isdigit():
                    raise Ex.NumericError
                elif ord(credit_choice) != 97 and ord(credit_choice) != 65 and ord(credit_choice) != 98 and ord(
                        credit_choice) != 66:
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
        if credit_choice == 'a' or credit_choice == 'A':
            accnt=self.Take_Account()
            print(f'Payment has been done successfully by account no. {accnt}')
        elif credit_choice == 'b' or credit_choice == 'B':
            print()
            print('Enter your EasyPaisa account number')
            e_accnt=self.Take_Account()
            print(f'Payment has been done successfully by account number {e_accnt}')
    @staticmethod
    def Take_Account():
        '''This method simply takes and returns the account from user and handles the exceptions accordingly'''
        while True:
            try:
                print()
                accnt = input('Please enter your account number: ')
                if accnt == '':
                    raise Ex.NoValue
                elif not accnt.isdigit():
                    raise Ex.AlphabeticError
            except Ex.NoValue:
                print()
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                continue
            except Ex.AlphabeticError:
                print('Enter Numbers please')
            else:
                return accnt