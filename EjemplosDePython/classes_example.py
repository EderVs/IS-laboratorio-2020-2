""" Classes example using inheritance. """

class Animal:
    """ Represents an animal. """

    def __init__(self, age):
        """ Animal constructor """
        self.age = age

    def breathe(self):
        """ Breathes """
        print("Breathing")

    def eat(self, meal):
        """ Eats the meal that is sent. """
        self.breathe()
        print("Eating " + meal)
        self.breathe()
    
class Person(Animal):
    """ Represents a person with a job. """
    job_office = ""

    def __init__(self, age, job_office="Home"):
        """ Person constructor. """
        self.job_office = job_office
        Animal.__init__(self, age)

    def work(self):
        """ Works in a place """
        self.breathe()
        print("Working at " + self.job_office)
        self.eat("Lunch")


person1 = Person(10)
person2 = Person(25, job_office="Pedregal")
person1.work()
person2.work()
