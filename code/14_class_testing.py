class Person:
    def __init__(self, num):
        self.age = 20
        self.name = 'do not know'
        self.num = num

    @property
    def age(self,):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age


person = Person(3)
print("age", person.age)
person.age = 10
print("age", person.age)
print(person.num)
person.num = 33 # bad
print(person.num)

