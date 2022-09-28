from datetime import datetime


def action_logger(data, ch):
    time = datetime.now().strftime('%H:%M:%S')
    if ch == '1':
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(f'Импорт контакта в {time}.{data}\n')
    elif ch == '2':
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(f'Экспорт контактов в {time}.{data}\n')
    elif ch == '3':
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(f"Поиск контакта в {time}.{data}\n")
