from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


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

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    all_planets = Planet.query.all()
    for planet in all_planets:
        # planets_response.append({
        #     "id": planet.id,
        #     "name": planet.name,
        #     "description": planet.description,
        #     "number of moons": planet.number_of_moons
        # })
        planets_response.append(planet.to_dict())
    return jsonify(planets_response), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    chosen_planet = get_planet_from_id(planet_id)
    return jsonify(chosen_planet.to_dict()), 200

@planets_bp.route("", methods=["POST"])
def create_one_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"], description=request_body["description"], number_of_moons=request_body["number_of_moons"])
    db.session.add(new_planet)
    db.session.commit()
    return jsonify({"msg": f"Successfully created planet with id={new_planet.id}"}), 201


@planets_bp.route('/<planet_id>', methods=['PUT'])
def update_one_planet(planet_id):
    update_planet = get_planet_from_id(planet_id)

    request_body = request.get_json()

    try:
        update_planet.name = request_body["name"]
        update_planet.description = request_body["description"]
        update_planet.number_of_moons = request_body["number_of_moons"]
    except KeyError:
        return jsonify({"msg": "Missing needed data"}), 400

    db.session.commit()
    return jsonify({"msg": f"Successfully updated planet with id {update_planet.id}"}), 200


@planets_bp.route('/<planet_id>', methods=['DELETE'])
def delete_one_planet(planet_id):
    planet_to_delete = get_planet_from_id(planet_id)

    db.session.delete(planet_to_delete)
    db.session.commit()

    return jsonify({"msg": f"Successfully deleted planet with id {planet_to_delete.id}"}), 200



def get_planet_from_id(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return abort(make_response({"msg": f"Invalid data type: {planet_id}"}), 400)
    chosen_planet = Planet.query.get(planet_id)
    if chosen_planet is None:
        return abort(make_response({"msg": f"Could not find planet with id: {planet_id}"}), 404)
    return chosen_planet








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
