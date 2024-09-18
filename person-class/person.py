class Person:
    def __init__(self, name, age, sex):
        self.name = name  # This variable shall store the nane of the 'person'
        self.age = age    # This variable shall store the age of the 'person'
        self.gender = sex # This variable shall store the gender of the 'person'

    def introduce(self):  #Implement a method called introduce that prints a message introducing the person with their name, age, and gender.
        print(f"Hello, my name is {self.name}, a {self.age} years old {self.gender}.")  

# Example:
person1 = Person("Hellen", 30, "female")
person1.introduce()  # Create an instance of the Person class and call the introduce method to display the person's information.


