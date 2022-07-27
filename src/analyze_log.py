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


def analyze_log(path_to_file):
    read(path_to_file)
