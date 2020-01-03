from flask import Blueprint, request, make_response, jsonify
user_module = Blueprint('user', __name__)
from src.usecases.interactor.user_usecase_impl import UserUseaseImpl
from src.repository.user_repository_impl import UserRepositoryImpl
from src.domain.model.user import User, users_schema

# user_module = Blueprint('user', __name__)

@user_module.route('/user', methods=['POST'])
def save():
    data = request.json['user']
    user = User(email=data['email'], password=data['password'], destination=data['email'])
    UserUseaseImpl(UserRepositoryImpl()).save(user)

@user_module.route('/users')
def get_all():
    users = UserUseaseImpl(UserRepositoryImpl()).get_all()
    return users_schema.dump(users)
    # print(users)
    # return make_response(jsonify({
    #     'code': 200,
    #     'users': users
    # }))
