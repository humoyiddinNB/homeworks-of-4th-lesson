import os
os.system("cls")

###     Bismillah 😊

class Dish:
    def __init__(self, dish_name, price, portion=1, calory="Not defined", category=None, description="Not Provided"):
        self.name = dish_name
        self.price = price
        self.portion = portion
        self.calory = calory
        self.category = category
        self.description = description

    def __str__(self):
        return f"""
Name of dish:   {self.name}
price of dish:  {self.price}
Available portions:  {self.portion}
Calory of dish:  {self.calory}
Type of dish:  {self.category}
Information about dish:  {self.description}
                  """


class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def get_menu(self):
        if not self.dishes:
            print("Unfortunately, there are no available dishes . Please, add dishes to Menu 😊")
            return
        print("        MENU:")
        for dish in self.dishes:
            print(f"""
Name of dish:   {dish.name}
price of dish:  {dish.price}
Available portions:  {dish.portion}
Calory of dish:  {dish.calory}
Type of dish:  {dish.category}
Information about dish:  {dish.description}
                  """)
            
    def remove_dish(self, name):
        for dish in self.dishes:
            if dish.name == name:
                self.dishes.remove(dish)
                info = f"{dish.name} removed from Menu"
                return info
        return f"Unfortunately, there is no dishe like that 😞"
    
    
class Order:
    def __init__(self, menu):
        self.menu = menu
        self.selected_dishes = []
        
    def add_to_order(self, dish_name, portion):
        for dish in self.menu.dishes:
            if dish.name == dish_name:
                if dish.portion >= portion:
                    dish.portion -= portion
                    self.selected_dishes.append(dish)
                    print(f"{dish.name} added orders!")
                else:
                    print(f"Available dishes are less than {portion}")
                return
        print("There is no dish like that 😞")
        
    def remove(self, dish_name):
        for dish in self.selected_dishes:
            if dish.name == dish_name:
                self.selected_dishes.remove(dish)
                for dish1 in self.menu:
                    if dish1 == dish_name:
                        dish1.portion += dish.portion
                print(f"{dish.name} removed from orders")
                return
        print(f"{dish_name} not find")
        
    def get_orders(self):
        print("     Your orders:")
        for dish in self.selected_dishes:
            print(f"""
Name of dish:   {dish.name}
price of dish:  {dish.price}
Available portions:  {dish.portion}
Calory of dish:  {dish.calory}
Type of dish:  {dish.category}
Information about dish:  {dish.description}
                  """)

    def get_prices(self):
        return sum(dish.price for dish in self.selected_dishes)
       
            
class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        
    def __str__(self):
        return f"Name:  {self.name}, Tephone:   {self.phone}"


class DeliveryPerson:
    def __init__(self, name, vehicle_num):
        self.name = name
        self.vehicle_num = vehicle_num
        
    def __str__(self):
        return f"Name:  {self.name}, Vehicle number:   {self.vehicle_num}"
    
# overal_menu = Menu()
 
    
# food1 = Dish("Plov", 15000, portion=10, calory=600, category="Main Course", description="Traditional Uzbek dish.")
# food2 = Dish("Shurva", 12000, portion=120, calory=400, category="Soup", description="Uzbek soup with vegetables and meat.")
# food3 = Dish("Lagman", 18000, portion=19, calory=700, category="Main Course", description="Central Asian noodle dish.")
# food4 = Dish("Manti", 14000, portion=10, calory=350, category="Main Course", description="Steamed dumplings with meat.")
# food5 = Dish("Somsa", 8000, portion=240, calory=300, category="Snack", description="Uzbek pastry with meat or pumpkin filling.")
# food6 = Dish("Kebab", 20000, portion=90, calory=500, category="Main Course", description="Grilled meat skewer.")
# food7 = Dish("Chuchvara", 10000, portion=69, calory=400, category="Soup", description="Uzbek dumpling soup.")
# food8 = Dish("Norin", 13000, portion=35, calory=600, category="Main Course", description="Cold noodles with horse meat.")
# food9 = Dish("Shashlik", 16000, portion=68, calory=550, category="Main Course", description="Grilled meat served with onions.")
# food10 = Dish("Honim", 12000, portion=65, calory=300, category="Main Course", description="Steamed rolled dough with vegetables.")


# dishes = [food1, food2, food3, food4, food5, food6, food7, food8, food9, food10]

# for dish in dishes:
#     overal_menu.add_dish(dish)
    
# overal_menu.get_menu()

# oreder1 = Order(overal_menu)
# oreder1.add_to_order("Norin", 30)
# oreder1.add_to_order("Shashlik", 68)

# overal_menu.get_menu()
