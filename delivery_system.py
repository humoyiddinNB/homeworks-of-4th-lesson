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
        for dish in self.menu:
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
        
    def print_orders(self):
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