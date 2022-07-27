import csv


def read(path):
    if not path.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: {path}")
    try:
        data_csv = []
        with open(path, "r", encoding="utf-8") as file:
            for row in csv.reader(file):
                data_csv.append(row)
        return data_csv

    except FileExistsError:
        raise FileNotFoundError(f"Arquivo inexistente: {path}")


def analyze_log(path_to_file):
    read(path_to_file)
