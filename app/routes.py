from flask import Blueprint

class Planet():
    def __init__(self, id, name, description, number_of_moons):
        self.id = id
        self.name = name
        self.description = description
        self.number_of_moons = number_of_moons


planet1 = Planet(1, "Mars", "4th planet from the sun", 2)
planet2 = Planet(2, "Jupiter", "5th planet from the sun", 80)
planet3 = Planet(3, "Saturn", "6th planet from the sun", 82)

planet_list = [planet1, planet2, planet3]

#please save this :)  I did it but just to make sure.