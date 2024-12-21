import os
os.system("cls")

###     Bismillah 😊

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"meal:    {self.name}\nprice:    {self.price}"


class Menu:
    def __init__(self):
        self.dishes = []
    
    def add_dish(self, dish_name, price, portion=1, calory="Not defined", category=None, description="Not Provided"):
        dish = {
            "name" : dish_name,
            "price" : price,
            "portion" : portion,
            "calory" : calory,
            "category" : category,
            "description" : description           
        }
        self.dishes.append(dish)

    def get_menu(self):
        if not self.dishes:
            return "Unfortunately, there are no dishes on Menu. Please, add food to the menu 😊"
        print("        MENU:")
        for dish in self.dishes:
            print(f"""
Name of dish:   {dish["name"]}
price of dish:  {dish["price"]}
Available portions:  {dish["portion"]}
Calory of dish:  {dish["calory"]}
Type of dish:  {dish["catogory"]}
Description of dish:  {dish["description"]}
                  """)
            
    def remove_dish(self, name):
        for dish in self.dishes:
            if dish["name"] == name:
                self.dishes.remove(dish)
                info = f"{dish["name"]} removed from Menu"
                return info