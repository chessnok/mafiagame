from flask import Blueprint, request

from models import User, db

routes = Blueprint("routes", __name__)


@routes.route(
    "/create_user",
    methods=["POST"],
)
def create_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    if not (username and email and password):
        return {"message": "Required fields are not filled in"}, 404
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return {"message": "User created successfully"}, 201


@routes.route("/get_user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return {"message": "User not found"}, 404
    return user.to_json(), 200
