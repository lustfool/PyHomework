def import_data(data, sep=';'):
    with open('base.csv', 'a+') as file:
        file.write(sep.join(data))
        file.write(f"\n")