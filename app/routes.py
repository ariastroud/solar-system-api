from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"{planet_id} is not a valid planet id"}, 400))

    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response({"message": f"{planet_id} not found"}, 404))
    
    return planet

@planet_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)

    return jsonify(planet.to_json()), 200

@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"], description=request_body["description"], size=request_body["size"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


@planet_bp.route("", methods=["GET"])
def handle_planets():
    planets = Planet.query.all()
    planets_response = [planet.to_json() for planet in planets]
    return jsonify(planets_response)

