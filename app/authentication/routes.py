from app import web
from flask import request, abort
from user import User

@web.route("/login", methods=["POST"])
def login():
    params = request.get_json()

    if not params or 'username' not in params or 'password' not in params:
        abort(400)

    valid_user = User.getAuthUser(params['username'], params['password'])

    if not valid_user:
        abort(403)

    return valid_user.generateToken(), {'Content-Type': 'text/plain'}