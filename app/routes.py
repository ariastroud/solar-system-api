from unicodedata import name
from flask import Blueprint, jsonify, abort, make_response

class Planet:

    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size
    
    def to_json(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            size=self.size
            )

planets = [
    Planet(1, "mercury", "the first planet", "small"),
    Planet(2, "earth", "our planet", "medium"),
    Planet(3, "jupiter", "a large planet", "large")
]

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET"])
def handle_planets():
    planets_list = []
    for planet in planets:
        planets_list.append(planet.to_json())
    return jsonify(planets_list)

@planet_bp.route("/<id>", methods=["GET"])
def handle_planet(id):
    planet = validate_planet(id)
    return jsonify(planet.to_json())

def validate_planet(id):
    try:
        planet_id = int(id)
    except:
        abort(make_response({"message": f"planet {id} invalid"}, 400))

    for planet in planets:
        if planet_id == planet.id:
            return planet
    abort(make_response({"message": f"planet {id} not found"}, 404))
