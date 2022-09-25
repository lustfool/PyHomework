def export_data():
    with open('base.csv', 'r') as file:
        data = []
        for line in file:
            temp = line.strip().split(';')
            data.append(temp)
    return data