import csv


def read(path):
    if not path.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: {path}")
    try:
        data = []
        with open(path, "r") as file:
            for line in csv.reader(file):
                data.append(line)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path}")


def most_requested_dish(user, data):
    dict_dish = dict()
    for client, dish, _ in data:
        if user == client:
            if dish in dict_dish:
                dict_dish[dish] += 1
            else:
                dict_dish[dish] = 1
    return max(dict_dish.items(), key=lambda x: x[1])[0]


def times_per_dish(user, request, data):
    dict_times = dict()
    for client, dish, _ in data:
        if user == client:
            if request == dish:
                if dish in dict_times:
                    dict_times[dish] += 1
                else:
                    dict_times[dish] = 1
    return dict_times[dish]


def dish_never_requested(user, data):
    all_dishes = set()
    dish_by_user = set()
    for _, dish, _ in data:
        all_dishes.add(dish)
    for client, dish, _ in data:
        if user == client:
            dish_by_user.add(dish)
    return all_dishes.difference(dish_by_user)


def day_without_order(user, data):
    all_days = set()
    days_visited = set()
    for _, _, day in data:
        all_days.add(day)
    for client, _, day in data:
        if client == user:
            days_visited.add(day)
    return all_days.difference(days_visited)


def analyze_log(path_to_file):
    file = read(path_to_file)
    most_requested = most_requested_dish("maria", file)
    times_dish = times_per_dish("arnaldo", "hamburguer", file)
    never_asked = dish_never_requested("joao", file)
    never_visited_by_client = day_without_order("joao", file)
    with open("data/mkt_campaign.txt", "w") as f:
        f.write(
            f"{most_requested}\n"
            f"{times_dish}\n"
            f"{never_asked}\n"
            f"{never_visited_by_client}\n"
        )
