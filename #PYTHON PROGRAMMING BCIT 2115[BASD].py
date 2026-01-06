#“There is a proposal to come up with a simple system which will have two classes. One of the classes is the base 
# class while the other is the sub class. The base class will store three data members namely product name, quantity and price.
#  The sub class will have two member methods, one of the methods will read the values of the data members
#  then pass those values to another method which calculates the cost of the product inclusive of the value added tax (VAT) 
# and displays the result”.
# Design an UML class diagram for this case.
# Implement the design above using python and instantiate the class with at least one object
class Item:
    def __init__(self,product_name = "",quantity=0,price=0.0):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        
class ItemCost(Item):
    def enter_details(self):
        self.product_name = str(input("Enter the name of the product: "))
        self.quantity = int(input("Enter the quantity: "))
        self.price = float(input("Enter the amount:"))

        self.calculate_total()
    
    def calculate_total(self):
        VAT = 0.16
        total_cost = self.quantity* self.price
        Vat_value = total_cost * VAT
        Overall_cost = total_cost + Vat_value

        print("\n---Item cost output---\n")
        print("Enter the name of the product:", self.product_name )
        print("Enter the quatity: ", self.quantity)
        print("Enter price:", self.price)
        print("VAT 16%:", Vat_value) 
        print("Overall cost:",Overall_cost) 

item1 = ItemCost()
print("\n---Product 1---")
item1.enter_details()

item2 = ItemCost()
print("\n---Product 2---")
item2.enter_details()

item3 = ItemCost()
print("\n---Product 3---")
item3.enter_details()

