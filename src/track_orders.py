from src.analyze_log import (
    most_requested_dish,
    dish_never_requested,
    day_without_order,
)


class TrackOrders:

    def __init__(self):
        self.orders = list()
        self.days = dict()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        return most_requested_dish(customer, self.orders)

    def get_never_ordered_per_customer(self, customer):
        return dish_never_requested(customer, self.orders)

    def get_days_never_visited_per_customer(self, customer):
        return day_without_order(customer, self.orders)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
