from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")

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

