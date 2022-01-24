from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


AllMenu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()
while True:
    order = input(f"What would you like?({AllMenu.get_items()}): ")
    if order == "off":
        break
    if order == "report":
        cm.report()
        mm.report()
        continue
    ordered_item = AllMenu.find_drink(order)
    if ordered_item:
        if cm.is_resource_sufficient(ordered_item):
            if mm.make_payment(ordered_item.cost):
                cm.make_coffee(ordered_item)

print("Coffee Machine OFF")
        