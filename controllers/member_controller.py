from flask import request
from services.member_service import MemberService
from services.order_service import OrderService

class MemberController:
    def __init__(self):
        self.memberService = MemberService()
        self.orderService = OrderService()

    def join(self):
        try:
            if request.environ.get('HTTP_AUTHORIZATION') is '':
                return {
                    'code': '8888',
                    'message': 'Invalid Access Key'
                }, 401

            result = self.memberService.join(request.form)
            if result is True:
                return {
                    'code': '0000',
                    'message': 'Member Join Success'
                }, 201
            else:
                return {
                    'code': '9998',
                    'message': result
                }, 409

        except Exception as e:
            return {
                'code': '9999',
                'message': 'Internal Server Error :: ' + str(e)
            }, 500

    def memberDetail(self, member_idx):
        try:
            if request.environ.get('HTTP_AUTHORIZATION') is '':
                return {
                    'code': '8888',
                    'message': 'Invalid Access Key'
                }, 401

            result = self.memberService.show(member_idx)
            if result is None:
                return {
                    'code': '9998',
                    'message': 'No Data'
                }, 200
            elif type(result) is dict:
                return {
                    'code': '0000',
                    'message': 'Member Info Success',
                    'data': result
                }, 200
            else:
                return {
                    'code': '9999',
                    'message': result
                }, 500

        except Exception as e:
            return {
                'code': '9999',
                'message': 'Internal Server Error :: ' + str(e)
            }, 500

    def memberOrders(self, member_idx):
        try:
            if request.environ.get('HTTP_AUTHORIZATION') is '':
                return {
                    'code': '8888',
                    'message': 'Invalid Access Key'
                }, 401

            result = self.orderService.list(member_idx)
            if result is None:
                return {
                    'code': '9998',
                    'message': 'No Data'
                }, 200
            elif type(result) is list:
                return {
                    'code': '0000',
                    'message': 'Member Order List Success',
                    'data': result
                }, 200
            else:
                return {
                    'code': '9999',
                    'message': result
                }, 500

        except Exception as e:
            return {
                'code': '9999',
                'message': 'Internal Server Error :: ' + str(e)
            }, 500

    def memberList(self):
        try:
            if request.environ.get('HTTP_AUTHORIZATION') is '':
                return {
                    'code': '8888',
                    'message': 'Invalid Access Key'
                }, 401

            result = self.memberService.list(request.args)
            if result is None:
                return {
                    'code': '9998',
                    'message': 'No Data'
                }, 200
            elif type(result) is list:
                return {
                    'code': '0000',
                    'message': 'Member List Success',
                    'data': result
                }, 200
            else:
                return {
                    'code': '9999',
                    'message': result
                }, 500

        except Exception as e:
            return {
                'code': '9999',
                'message': 'Internal Server Error :: ' + str(e)
            }, 500