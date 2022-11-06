from app import db
from app.models.planet import Planet
from app.models.moon import Moon
from flask import Blueprint, jsonify, abort, make_response, request

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"{cls.__name__} {model_id} is not a valid id"}, 400))

    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message": f"{cls.__name__} {model_id} not found"}, 404))
    
    return model

@planet_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return jsonify(planet.to_dict()), 200

@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planet_bp.route("", methods=["GET"])
def handle_planets():
    name_query = request.args.get("name")
    size_query = request.args.get("size")

    planet_query = Planet.query

    if name_query:
        planet_query = planet_query.filter_by(name=name_query) 

    if size_query:
        planet_query = planet_query.filter_by(size=size_query)

    planets = planet_query.all()
    planets_response = [planet.to_dict() for planet in planets]
    return jsonify(planets_response)

@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.size = request_body["size"]
    planet.description = request_body["description"]

    db.session.commit()

    return make_response(f"Planet {planet.id} successfully updated"), 200

@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} successfully deleted"), 200

# create a Moon and link it to an existing Planet record
@planet_bp.route("/<planet_id>/moons", methods=["POST"])
def create_moon(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()
    new_moon = Moon.from_dict(request_body)
    new_moon.planet = planet

    db.session.add(new_moon)
    db.session.commit()

    return make_response(f"Moon {new_moon.name} is a moon of {planet.name}", 201)