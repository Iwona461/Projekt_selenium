class Restauracja():
    """Modelowanie psa"""

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f'Atutem Restauracji "{self.name.title()}" jest typowa {self.type}.')

    def open_restaurant(self):
        print(f'"{self.name.title()}" czynne jest w godzinach 10am-23pm przez 7 dni w tygodniu')

my_restaurant = Restauracja('Bocianie Gniazdo', 'kuchnia polska')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

sec_restaurant = Restauracja('Czerwona Róża', 'kuchnia orientalna')
sec_restaurant.describe_restaurant()

third_restaurant = Restauracja('Czerwony Wieprz', 'kuchnia meksykańska')
third_restaurant.describe_restaurant()
