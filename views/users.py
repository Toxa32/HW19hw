from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from decorators import admin_required
from implemented import user_service


user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):

    def get(self):
        rs = user_service.get_all()
        res = UserSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        req_json = request.json
        new_user = user_service.create(**req_json)
        return "", 201, {"location": f"/users/"}


@user_ns.route('/<int:rid>')
class UserView(Resource):

    def get(self, rid):
        r = user_service.get_one(rid)
        sm_d = UserSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, rid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = rid
        user_service.update(req_json)
        return "", 204
    @admin_required
    def delete(self, rid):
        user_service.delete(rid)
        return "", 204
