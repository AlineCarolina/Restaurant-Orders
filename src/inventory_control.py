class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }

    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):

        self.inventory = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }

        self.orders = list()

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self.inventory[ingredient] == 0:
                return False
            self.inventory[ingredient] -= 1
        self.orders.append((customer, order, day))

    def get_quantities_to_buy(self):
        to_buy = dict()
        for ingredient in self.inventory:
            to_buy[ingredient] = (
                self.MINIMUM_INVENTORY[ingredient] - self.inventory[ingredient]
            )
        return to_buy

    def get_available_dishes(self):
        available_ingredients = set()
        available_dishes = set()

        for ingredient in self.inventory:
            if self.inventory[ingredient] > 0:
                available_ingredients.add(ingredient)

        for dish, ingredients in self.INGREDIENTS.items():
            if set(ingredients).issubset(available_ingredients):
                available_dishes.add(dish)
        return available_dishes
