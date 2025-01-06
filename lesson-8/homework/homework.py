class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")
