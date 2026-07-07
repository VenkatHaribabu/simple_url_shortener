from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from models import insert_url, get_url
from schemas import URLSchema
from tasks import validate_url_task
from utils import generate_short_code

api = Blueprint("api", __name__)
schema = URLSchema()


@api.route("/shorten", methods=["POST"])
def shorten_url():
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    original_url = data["url"]
    short_code = generate_short_code()
    url_id = insert_url(short_code, original_url)
    message = {
        "id": url_id,
        "short_code": short_code,
        "url": original_url
    }
    validate_url_task.delay(message)

    return jsonify({
        "id": url_id,
        "short_code": short_code,
        "url": original_url
    }), 202


@api.route("/url/<short_code>", methods=["GET"])
def get_url_details(short_code):
    row = get_url(short_code)
    if row is None:
        return jsonify({
            "message": "Short code not found"
        }), 404

    return jsonify({
        "short_code": row["short_code"],
        "original_url": row["original_url"],
        "status": row["status"]
    }), 200