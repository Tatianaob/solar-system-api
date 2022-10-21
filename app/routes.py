from flask import Blueprint, jsonify

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

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planet_list:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "number of moons": planet.number_of_moons
        })
    return jsonify(planets_response)

#please save this :)  I did it but just to make sure.