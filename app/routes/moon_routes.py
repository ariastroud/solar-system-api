from app import db
from app.models.moon import Moon
from flask import Blueprint, jsonify, abort, make_response, request

moon_bp = Blueprint("moon", __name__, url_prefix="/moons")