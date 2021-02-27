print("Задание 2")

name = input('Введите имя')
surname = input('Введите фамилию')
year = int(input('Ваш год рождения'))
city = input('Ваш город проживания')
email = input('Ваша электронная почта')
telephone = input('Ваш номер телефона')

def my_func(name, surname, year, city, email, phone):
    return ' '.join([name, surname, year, city, email, phone])

print(my_func(name='', surname='', year='', city='', email='', phone=''))