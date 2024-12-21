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
