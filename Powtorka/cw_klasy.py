#Tworzenie klasy
#nazwa klasy zawsze z dużej litery. Nawias w definicji klasy jest pusty, gdyż tworzymy ją od samego początku

class Dog():
    """Modelowanie psa"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name.title()} teraz siedzi.")

    def roll_over(self):
        print(f"{self.name.title()} teraz się położyła.")

my_dog = Dog('Axa', 8)
second_dog = Dog('Dyzio', 10)

print(f"Mój mniejszy pies ma na imię {my_dog.name.title()}.")
print(f"{my_dog.name.title()} ma {my_dog.age} lat.")
my_dog.sit()
print(f"Mój większy pies ma na imię {second_dog.name.title()}.")
print(f"{second_dog.name.title()} ma {second_dog.age} lat.")
second_dog.roll_over()
