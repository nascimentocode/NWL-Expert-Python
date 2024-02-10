from flask import Blueprint, request, jsonify
from src.views.http_types.http_requests import HttpRquest
from src.views.tag_creator_view import TagCreatorView

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=["POST"])
def create_tags():
    tag_creator_view = TagCreatorView()

    http_request = HttpRquest(body=request.json)
    response = tag_creator_view.validate_and_create(http_request)

    return jsonify(response.body), response.status_code
