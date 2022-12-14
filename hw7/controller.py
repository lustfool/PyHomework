from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data
from input_data import input_data
from logger import *

def greeting():
    print("Здравствуйте!")


def choice_todo():
    print("Выберите действие:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта.")
    ch = input("Введите цифру: ")
    if ch == '1':
        data = input_data()
        import_data(data)
        action_logger(data, '1')
    elif ch == '2':
        data = export_data()
        action_logger(data, '2')
        print_data(data)
    elif ch == '3':
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        action_logger(item, '3')
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
            print("-" * 85)
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
        else:
            print("Данные не обнаружены")
