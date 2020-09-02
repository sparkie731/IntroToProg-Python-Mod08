<<<<<<< HEAD
# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# EPark,8.26.2020, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# - - - - - - - Data - - - - - - - #
FileName = 'products.txt'
lstOfProductObjects = []

class Product(object):
    # Fields: Not needed in this case

    # Constructors
    def __init__(self, product_name, product_price):
    # Attributes
        self.productname = product_name
        self.productprice = product_price

    # properties for product name
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self,value):
        if str(value).isnumeric() == False:
            self.product_name = value
        else:
            raise Exception ("Product Name must be a number")

    # properties for product price
    #getter
    @property
    def product_price(self):
        return (self.__product_price)

    #setter
    @product_price.setter
    def product_name(self,value):
        if float(value).isnumeric()== True:
            self.product_name = value
        else:
            raise Exception ("Price must be numeric")

# Processing  ------------------------------------------------------------- #
class FileProcessor:

    #Code to process data from a file
    def Read_file(file_name):
        lstTable=[]
        file = open(file_name, "r")
        for line in file:
            product_name,product_price = line.split(",")
            row = Product(str(product_name),str(product_price))
            lstTable.append(row)
        file.close()
        return lstTable


    #Code to process data to a file
    def Write_file(file_name,lstTable):
        file = open(file_name, "w")
        for row in lstTable:
            file.write(row[0], row[1],"\n")
        file.close()


# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    pass

    #Code to show menu
    def show_menu():
        print('''
        Please Select
        1. Show Current Product List
        2. Add Product Entry
        3. Save Product List
        4. Exit
        ''')

    # Code to get user's choice
    def menu_select():
        user_choice = input("select from menu:")
        return user_choice

    # Code to show the current data from the file to user
    def ShowProducts():
        lstData = list(lstTable)
        for product in lstData:
            print(lstData)


    # Code to get product data from user
    def NewProduct():
        new_product = input("Enter new product name: ")
        new_price = input("Enter the new product price: ")

# - - - - - - - Main Body of Script - - - - - - -#

# Load data from file into a list of product objects when script starts
lstTable = FileProcessor.Read_file(FileName)

while(True):
    # Show user a menu of options
    IO.show_menu()
    strChoice = IO.menu_select()

    if strChoice=="1":
        IO.ShowProducts()
    elif strChoice=="2":
        IO.NewProduct()
    elif strChoice=="3":
        FileProcessor.Write_file(FileName,lstTable)
    elif strChoice=="4":
        print("Exiting program")
        break



# Get user's menu option choice
# Show user current data in the list of product objects
# Let user add data to the list of product objects
# let user save current data to file and exit program


# Main Body of Script  ---------------------------------------------------- #

=======
# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# EPark,8.26.2020, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# - - - - - - - Data - - - - - - - #
FileName = 'products.txt'
lstOfProductObjects = []

class Product(object):
    # Fields: Not needed in this case

    # Constructors
    def __init__(self, product_name, product_price):
    # Attributes
        self.productname = product_name
        self.productprice = product_price

    # properties for product name
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self,value):
        if str(value).isnumeric() == False:
            self.product_name = value
        else:
            raise Exception ("Product Name must be a number")

    # properties for product price
    #getter
    @property
    def product_price(self):
        return (self.__product_price)

    #setter
    @product_price.setter
    def product_name(self,value):
        if float(value).isnumeric()== True:
            self.product_name = value
        else:
            raise Exception ("Price must be numeric")

# Processing  ------------------------------------------------------------- #
class FileProcessor:

    #Code to process data from a file
    def Read_file(file_name):
        lstTable=[]
        file = open(file_name, "r")
        for line in file:
            product_name,product_price = line.split(",")
            row = Product(str(product_name),str(product_price))
            lstTable.append(row)
        file.close()
        return lstTable


    #Code to process data to a file
    def Write_file(file_name,lstTable):
        file = open(file_name, "w")
        for row in lstTable:
            file.write(row[0], row[1],"\n")
        file.close()


# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    pass

    #Code to show menu
    def show_menu():
        print('''
        Please Select
        1. Show Current Product List
        2. Add Product Entry
        3. Save Product List
        4. Exit
        ''')

    # Code to get user's choice
    def menu_select():
        user_choice = input("select from menu:")
        return user_choice

    # Code to show the current data from the file to user
    def ShowProducts():
        lstData = list(lstTable)
        for product in lstData:
            print(lstData)


    # Code to get product data from user
    def NewProduct():
        new_product = input("Enter new product name: ")
        new_price = input("Enter the new product price: ")

# - - - - - - - Main Body of Script - - - - - - -#

# Load data from file into a list of product objects when script starts
lstTable = FileProcessor.Read_file(FileName)

while(True):
    # Show user a menu of options
    IO.show_menu()
    strChoice = IO.menu_select()

    if strChoice=="1":
        IO.ShowProducts()
    elif strChoice=="2":
        IO.NewProduct()
    elif strChoice=="3":
        FileProcessor.Write_file(FileName,lstTable)
    elif strChoice=="4":
        print("Exiting program")
        break



# Get user's menu option choice
# Show user current data in the list of product objects
# Let user add data to the list of product objects
# let user save current data to file and exit program


# Main Body of Script  ---------------------------------------------------- #

>>>>>>> 34a9789c6da52d87b3b91bf720640f30c880df9a
