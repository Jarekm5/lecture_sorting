import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

def read_data(path):
    dictio = {
    "series_1": [],
    "series_2": [],
    "series_3": []
    }
    with open(path) as file:
        readed = csv.DictReader(file)
        for row in readed:
            dictio["series_1"].append(int(row["series_1"]))
            dictio["series_2"].append(int(row["series_2"]))
            dictio["series_3"].append(int(row["series_3"]))
        return dictio

def selection_sort(readed_file):
    new_dict = {}
    for key, value in readed_file.items():
        n = 0
        i = 0
        j = 0
        n = len(value)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if value[j] < value[min_index]:
                    min_index = j
            value[i], value[min_index] = value[min_index], value[i]
        new_dict[key] = value
    return new_dict

def bubble_sort(readed_file):
    new_dict = {}
    new_list = []
    for key,value in readed_file.items():
        new_list = []
        new_list = value
        n = len(new_list)
        for i in range(n-1):
            if new_list[i] > new_list[i+1]:
                new_list[i] = value[i+1]
                new_list[i+1] = value[i]
        new_dict[key] = new_list
    return new_dict

def insertion_sort(readed):
    new_dict = {}
    listos = []
    for key,values in readed.items():
        listos = []
        n = len(values)
        for i in range(1, n):
            pos = values[i]
            j = i - 1
            while j >= 0 and pos < values[j]:
                values[j+1] = values[j]
                j -= 1
            listos.append(pos)
            new_dict[key] = listos
    print(new_dict)


def main(pathway):
    readerd = read_data(pathway)
    selection_sort(readerd)
    bubble_sort(readerd)
    insertion_sort(readerd)
    pass


if __name__ == '__main__':
    path = r"numbers.csv"
    main(path)


