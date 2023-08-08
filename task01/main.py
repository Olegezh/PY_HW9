#Напишите следующие функции: ○Нахождение корней квадратного уравнения
#○Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
#○Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
#○Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
from random import randint, uniform

filename = "test"

def json_saver(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(f'{file_name}.json', 'a') as file:
                temp_dict = {'args' : args}
                temp_dict.update(kwargs)
                result = func(*args, **kwargs)
                temp_dict['result'] = result
                json.dump(temp_dict, file, indent=3, ensure_ascii=False)
            return result
        return wrapper
    return decorator


def data_from_file(file_name):
    def decorator(func):
        def wrapper(*args):
            results = []

            with open(f"{file_name}.csv", "r") as file:
                data_read = csv.reader(file, delimiter=";")
                for row in data_read:
                    solution, x1, x2 = func(float(row[0]), float(row[1]), float(row[2]))
                    results.append((row[0], row[1], row[2], solution, x1, x2))
            return results

        return wrapper

    return decorator

@json_saver(filename)
@data_from_file(filename)
def find_root_of_equation(a: float, b: float, c: float):
    solution = True
    x1 = x2 = None
    if a == 0:
        x1 = x2 = c / b
    else:
        d = b * b - 4 * a * c
        if d < 0:
            solution = False
        else:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
    return solution, x1, x2


def csv_three_num_gen(file_name: str):
    iterations = randint(100, 1000)
    with open(f"{file_name}.csv", "w", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for i in range(iterations):
            a = uniform(-100, 100)
            b = uniform(-100, 100)
            c = uniform(-100, 100)

            writer.writerow((a, b, c))



csv_three_num_gen(filename)

find_root_of_equation()
