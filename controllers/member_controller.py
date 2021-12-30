from flask import request
from services.member_service import MemberService
from services.order_service import OrderService

class MemberController:
    def __init__(self):
        self.memberService = MemberService()
        self.orderService = OrderService()

    '''
    POST::/api/join
    회원가입

    @PARAMETER
        id          : 회원아이디 (영문 대문자 + 소문자 + 숫자)
        name        : 회원이름 (한글 + 영문 대문자 + 소문자)
        nick        : 회원별명 (영문 소문자만)
        password    : 회원비밀번호 (최소 10자, 영어 대문자/소문자/숫자/특수문자 각 1개 이상 포함)
        tel         : 전화번호 (최대 13자, 숫자만)
        email       : 이메일 (최대 100자)
        gender      : 성별 (M:남성, F:여성)
    
    @RETURN
        code        : 응답코드
        message     : 응답메세지
    '''
    def join(self):
        try:
            if request.environ.get('HTTP_AUTHORIZATION') == '':
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

    '''
    GET::/api/member/{member_idx}
    단일 회원 상세 정보 조회

    @PARAMETER
        member_idx              : 회원식별자
    
    @RETURN
        code                    : 응답코드
        message                 : 응답메세지
        data                    : 회원정보데이터
            member_idx          : 식별자
            member_id           : 아이디
            member_name         : 이름
            member_nickname     : 닉네임
            member_tel          : 전화번호
            member_email        : 이메일
            member_gender       : 성별 (M:남성, F:여성)
            join_datetime       : 회원가입일자
            last_login_datetime : 마지막로그인일자
    '''
    def memberDetail(self, member_idx):
        try:
            if request.environ.get('HTTP_AUTHORIZATION') == '':
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

    '''
    GET::/api/order/{member_idx}
    단일 회원의 주문 목록 조회

    @PARAMETER
        member_idx          : 회원식별자
    
    @RETURN
        code                : 응답코드
        message             : 응답메세지
        data                : 회원주문정보데이터
            order_no        : 주문번호
            product_name    : 상품명
            order_price     : 주문금액
            order_datetime  : 주문일시
            pay_datetime    : 결제일시
    '''
    def memberOrders(self, member_idx):
        try:
            if request.environ.get('HTTP_AUTHORIZATION') == '':
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

    '''
    GET::/api/order/{member_idx}
    여러 회원 목록 조회

    @PARAMETER
        page                    : 페이지번호
        id                      : 아이디
        email                   : 이메일
    
    @RETURN
        code                    : 응답코드
        message                 : 응답메세지
        data                    : 회원리스트데이터 (Array)
            member_idx          : 식별자
            member_id           : 아이디
            member_name         : 이름
            member_nickname     : 닉네임
            member_tel          : 전화번호
            member_email        : 이메일
            member_gender       : 성별 (M:남성, F:여성)
            join_datetime       : 회원가입일자
            last_login_datetime : 마지막로그인일자
            last_order_datetime : 마지막주문일자
    '''
    def memberList(self):
        try:
            if request.environ.get('HTTP_AUTHORIZATION') == '':
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