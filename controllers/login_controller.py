from flask import request
from services.member_service import MemberService

class LoginController:
    def __init__(self):
        self.memberService = MemberService()

    '''
    POST::/api/login
    로그인

    @PARAMETER
        id                      : 회원아이디
        password                : 회원비밀번호
    
    @RETURN
        code                    : 응답코드
        message                 : 응답메세지
        data                    : 
            member_idx          : 식별자
            member_id           : 아이디
            member_name         : 이름
            member_nickname     : 닉네임
            last_login_datetime : 마지막로그인일자
            login_token         : 로그인토큰
    '''
    def login(self):
        try:
            if request.environ.get('HTTP_AUTHORIZATION') == '':
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
                result["last_login_datetime"] = result["last_login_datetime"].strftime("%Y-%m-%d %H:%M:%S")
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

    '''
    POST::/api/login
    로그아웃

    @PARAMETER
        member_idx  : 식별자
        token       : 로그인토큰
    
    @RETURN
        code        : 응답코드
        message     : 응답메세지
    '''
    def logout(self):
        try:
            if request.environ.get('HTTP_AUTHORIZATION') == '':
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