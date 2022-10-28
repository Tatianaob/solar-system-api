from flask import Blueprint, jsonify



# class Planet():
#     def __init__(self, id, name, description, number_of_moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.number_of_moons = number_of_moons


# planet1 = Planet(1, "Mars", "4th planet from the sun", 2)
# planet2 = Planet(2, "Jupiter", "5th planet from the sun", 80)
# planet3 = Planet(3, "Saturn", "6th planet from the sun", 82)

# planet_list = [planet1, planet2, planet3]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# @planets_bp.route("", methods=["GET"])
# def handle_planets():
#     planets_response = []
#     for planet in planet_list:
#         planets_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "number of moons": planet.number_of_moons
#         })
#     return jsonify(planets_response)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_one_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError: 
#         return jsonify({"message":f"Invalid data type {planet_id}"}), 400
    
#     chosen_planet = None
#     for planet in planet_list:
#         if planet.id == planet_id:
#             chosen_planet = planet
        
#     if chosen_planet is None:
#         return jsonify({"message":f"Could not find planet with id {planet_id}"}), 404

#     return_planets = {
#         "id": chosen_planet.id,
#         "name": chosen_planet.name,
#         "description": chosen_planet.description,
#         "number of moons": chosen_planet.number_of_moons
#     }

#     return jsonify(return_planets), 200








