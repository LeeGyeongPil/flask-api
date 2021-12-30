from flask import request
from services.member_service import MemberService

class LoginController:
    def __init__(self):
        self.memberService = MemberService()

    def login(self):
        try:
            if request.environ.get('HTTP_AUTHORIZATION') is '':
                return {
                    'code': '8888',
                    'message': 'Invalid Access Key'
                }, 401

            result = self.memberService.login(request.form)
            if result is None:
                return {
                    'code': '2000',
                    'message': 'Login Fail'
                }, 200
            elif type(result) is dict:
                result['login_token'] = self.memberService.tokenRefresh(result)
                return {
                    'code': '0000',
                    'message': 'Login Success',
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

    def logout(self):
        try:
            if request.environ.get('HTTP_AUTHORIZATION') is '':
                return {
                    'code': '8888',
                    'message': 'Invalid Access Key'
                }, 401

            result = self.memberService.tokenValidation(request.form)
            if result is 0:
                return {
                    'code': '2000',
                    'message': 'Logout Fail'
                }, 200
            elif result is 1:
                self.memberService.tokenDelete(request.form['member_idx'])
                return {
                    'code': '0000',
                    'message': 'Logout Success',
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