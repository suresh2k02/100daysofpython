class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        opt=""
        for i in self.menu:
            opt += i.name + " "
            
        return opt
    
    def find_drink(self, order_name):
        for i in self.menu:
            if i.name == order_name:
                return i
        return None
            
        
        
        
        

""" ob=Menu()
ob.get_items()
print(ob.get_items())
a=ob.find_drink("latte")
if a==None:
    print("Sorry that item is not available.")
else:
    print(a.name) """






