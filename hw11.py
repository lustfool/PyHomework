class Person:
    def __init__(self, name, middlename, lastname, numbers):
        self.name = name
        self.lastname = lastname
        self.middlename = middlename
        self.numbers = numbers

    def get_phone(self):
        return self.numbers.get('private')

    def get_name(self):
        return f'{self.lastname} {self.name} {self.middlename}'

    def get_work_phone(self):
        return self.numbers.get('work')

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.middlename}! Примите участие в нашем беспроигрышном конкурсе для физических лиц.'


class Company:
    def __init__(self, title, ctype, company_numbers, *args):
        self.title = title
        self.ctype = ctype
        self.company_numbers = company_numbers
        self.persons = args

    def get_phone(self):
        if self.company_numbers.get("contact"):
            return self.company_numbers.get("contact")
        else:
            for person in self.persons:
                if person.get_work_phone():
                    return person.get_work_phone()
            return None

    def get_name(self):
        return self.title

    def get_sms_text(self):
        return f"Для компании {self.title} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для" \
               f" {self.ctype}"


def send_sms(*args):
    for i in args:
        if i.get_phone():
            print(f"Отправлено СМС на номер {i.get_phone()} с текстом {i.get_sms_text()}")
        else:
            print(f'Не удалось отправить сообщение абоненту: {i.get_name()}')


person1 = Person('Ivan', 'Ivanovich', 'Ivanov', {'private': 123, 'work': 456})
person2 = Person('Ivan', 'Petrovich', 'Petrov', {'private': 789})
person3 = Person('Ivan', 'Petrovich', 'Sidorov', {'work': 789})
person4 = Person('John', 'Unknown', 'Doe', {})
company1 = Company('Bell', 'ООО', {'contact': 111}, person3, person4)
company2 = Company('Cell', 'АО', {'non_contact': 222}, person2, person3)
company3 = Company('Dell', 'Ltd', {'non_contact': 333}, person2, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)

print()

person1 = Person('Степан', 'Петрович', 'Джобсов', {'private': 555})
person2 = Person('Боря', 'Иванович', 'Гейтсов', {'private': 777, 'work': 888})
person3 = Person('Семен', 'Робертович', 'Возняцкий', {'work': 789})
person4 = Person('Леонид', 'Арсенович', 'Торвальдсон', {})
company1 = Company('Яблочный комбинат', 'ООО', {'contact': 111}, person1, person2)
company2 = Company('ПластОкно', 'АО', {'non_contact': 222}, person2)
company3 = Company('Пингвинья ферма', 'Ltd', {'non_contact': 333}, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)
