from unicodedata import name
from flask import Blueprint, jsonify

class Planet:

    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size

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
        planets_list.append(dict
            (
            id=planet.id,
            name=planet.name,
            description=planet.description,
            size=planet.size
            )
        )
