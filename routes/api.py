from flask import Blueprint, request, jsonify
from flask_restx import Resource, Api, Namespace, fields
from flask_inputs import Inputs
from controllers.login_controller import LoginController
from controllers.member_controller import MemberController
from config.validation import *

ApiRoute = Blueprint('ApiRoute', __name__)

loginController = LoginController()
memberController = MemberController()

@ApiRoute.route('/login', methods=['POST'])
def login():
    inputs = LoginValidation(request)
    if not inputs.validate():
        return {
            'code': '1000',
            'message': inputs.errors[0]
        }, 400

    return loginController.login()

@ApiRoute.route('/logout', methods=['POST'])
def logout():
    inputs = LogoutValidation(request)
    if not inputs.validate():
        return {
            'code': '1000',
            'message': inputs.errors[0]
        }, 400

    return loginController.logout()

@ApiRoute.route('/join', methods=['POST'])
def join():
    inputs = JoinValidation(request)
    if not inputs.validate():
        return {
            'code': '1000',
            'message': inputs.errors[0]
        }, 400

    return memberController.join()

@ApiRoute.route('/member/<int:member_idx>', methods=['GET'])
def memberDetail(member_idx):
    return memberController.memberDetail(member_idx)

@ApiRoute.route('/order/<int:member_idx>', methods=['GET'])
def memberOrders(member_idx):
    return memberController.memberOrders(member_idx)

@ApiRoute.route('/member', methods=['GET'])
def memberList():
    return memberController.memberList()