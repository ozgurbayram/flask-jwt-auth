from app.api.auth import bp
from flask import jsonify, make_response, request
from app.models import User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required

@bp.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    user = User.query.filter_by(email=email).first()
    if user:
        if user.provider == 'social':
            access_token = create_access_token(user.email)
            return jsonify({"access_token":access_token}),200
        if user.check_password(password): 
            access_token = create_access_token(user.email)
            return jsonify({"access_token":access_token}),200
        else:
            return make_response('Wrong Password',400)
    else:
        return make_response('User is not found',400)

@bp.route('/register',methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    user = User.query.filter_by(email=email).first()

    if user:
        return make_response("User exist",409)
    else:
        if data['provider']:
            provider = data['provider']
            if provider == 'social':
                avatar = data['avatar']
                username = data['name']
                auth_token = data['auth_token']
                new_user = User(email=email,username=username,provider=provider,avatar=avatar,role='basic',auth_token=auth_token)
                new_user.save()
                acces_token = create_access_token(email)
                return jsonify({"access_token":acces_token}),200
            elif provider == 'web' or 'mobile':
                password = data['password']
                password_check = data['password_check']
                if password != password_check:
                    return make_response('Passwords are not match',400)
                else:
                    new_user = User(email=email,password=password,provider=provider)
                    new_user.set_password()    
                    new_user.save()
                    access_token = create_access_token(email)
                    return jsonify({"access_token":access_token}),200

@bp.route('/users')
@jwt_required()
def user():
    users = []
    user_list = User.query.all()
    for i in user_list:
        users.append(i.to_dict())

    return jsonify(users)