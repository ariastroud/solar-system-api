from app import db
from app.models.moon import Moon
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

moon_bp = Blueprint("moon", __name__, url_prefix="/moons")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response(
            {"message": f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    if not model:
        abort(make_response(
            {"message": f"{cls.__name__} {model_id} not found"}, 404))

    return model


@moon_bp.route("", methods=["POST"])
def create_moon():
    request_body = request.get_json()
    new_moon = Moon.from_dict(request_body)

    db.session.add(new_moon)
    db.session.commit()

    return make_response(f"Moon {new_moon.name} successfully created", 201)


@moon_bp.route("", methods=["GET"])
def read_all_moons():
    moons = Moon.query.all()

    moons_response = [moon.to_dict() for moon in moons]

    return jsonify(moons_response)