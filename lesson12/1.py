"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: 
        <Бренд-Модель> - Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""

class Phone:
    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.year = issue_year

    def receive_call(self, name):
        self.name = name
        print(f"{self.brand}-{self.model} - Звонит {self.name}")

    def get_info(self):
        self.cort = (self.brand, self.model, self.year)
        return self.cort
    
    def str(self):
        print(f'''
    Бренд: {self.brand}
    Модель: {self.model}
    Год выпуска: {self.year}
                             ''')
        
user1 = Phone('Apple', 'iphone 15', 2023)
user2 = Phone('Samsung', 'galaxy s24', 2024)

user1.receive_call('Иван')
user2.receive_call('Дарья')

print(user1.get_info())
print(user2.get_info())

user1.str()
user2.str()