from flask import Blueprint
from flask_restx import Resource, Api, Namespace, fields
from controllers.login_controller import LoginController
from controllers.member_controller import MemberController

ApiRoute = Blueprint('ApiRoute', __name__)

loginController = LoginController()
memberController = MemberController()

@ApiRoute.route('/login', methods=['POST'])
def login():
    return loginController.login()

@ApiRoute.route('/logout', methods=['POST'])
def logout():
    return loginController.logout()

@ApiRoute.route('/join', methods=['POST'])
def join():
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