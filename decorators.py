import jwt
from flask import request, abort

from constants import JWT_SECRET, JWT_ALGORITHM


def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorisation" not in request.headers:
            abort(401)

        data = request.headers["Authorisation"]

        token = data.split("Bearer")[-1]
        try:
            jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        except Exception as e:
            print("JWT Decode Exeption", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper
