import hashlib
import time
from config.database import Database

class MemberService:

    def __init__(self):
        self.perPage = 10
        self.db = Database()
    
    def join(self, request):
        try:
            query = 'INSERT INTO `Member` SET \
                        member_id = %(member_id)s, \
                        member_name = %(member_name)s, \
                        member_nickname = %(member_nickname)s, \
                        member_password = %(member_password)s, \
                        member_tel = %(member_tel)s, \
                        member_email = %(member_email)s, \
                        member_gender = %(member_gender)s'
            param = {
                'member_id': request['id'],
                'member_name': request['name'],
                'member_nickname': request['nick'],
                'member_password': hashlib.sha256(request['password'].encode()).hexdigest(),
                'member_tel': request['tel'],
                'member_email': request['email'],
                'member_gender': request['gender']
            }
            self.db.execute(query, param)
            self.db.commit()
            return True
        except Exception as e:
            return e

    def show(self, member_idx):
        try:
            query = 'SELECT \
                        member_idx, \
                        member_id, \
                        member_name, \
                        member_nickname, \
                        member_tel, \
                        member_email, \
                        member_gender, \
                        join_datetime, \
                        last_login_datetime \
                    FROM \
                        Member \
                    WHERE \
                        member_idx = %(member_idx)s'
            param = {
                'member_idx': member_idx
            }
            result = self.db.executeOne(query, param)
            return result
        except Exception as e:
            return e

    def list(self, request):
        try:
            query = 'SELECT \
                        Member.member_idx, \
                        Member.member_id, \
                        Member.member_name, \
                        Member.member_nickname, \
                        Member.member_tel, \
                        Member.member_email, \
                        Member.member_gender, \
                        Member.join_datetime, \
                        Member.last_login_datetime, \
                        Orders.order_datetime AS last_order_datetime \
                    FROM \
                        Member \
                    LEFT JOIN \
                        (SELECT member_idx, MAX(order_datetime) AS order_datetime FROM Orders GROUP BY member_idx) AS Orders \
                    ON \
                        Orders.member_idx = Member.member_idx \
                    WHERE \
                        1 = 1'
            param = {}
            if request.get('id', None):
                query = query + ' AND Member.member_id LIKE ' + '%(member_id)s'
                param['member_id'] = '%' + request['id'] + '%'


            if request.get('email', None):
                query = query + ' AND Member.member_email LIKE %(member_email)s'
                param['member_email'] = '%' + request['email'] + '%'

            page = (int(request.get('page', 1)) - 1) * self.perPage
            query = query + ' LIMIT ' + str(page) + ',' + str(self.perPage)
            result = self.db.executeAll(query, param)
            return result
        except Exception as e:
            return e

    def login(self, request):
        try:
            query = 'SELECT \
                        member_idx, \
                        member_id, \
                        member_name, \
                        member_nickname, \
                        last_login_datetime \
                    FROM \
                        Member \
                    WHERE \
                        member_id = %(member_id)s \
                        AND member_password = %(member_password)s'
            param = {
                'member_id': request['id'],
                'member_password': hashlib.sha256(request['password'].encode()).hexdigest()
            }
            result = self.db.executeOne(query, param)
            return result
        except Exception as e:
            return e

    def tokenRefresh(self, member):
        try:
            loginToken = hashlib.sha1((member['member_id'] + str(int(time.time())) + 'idus').encode()).hexdigest()
            query = 'UPDATE `Member` SET \
                        login_token = %(login_token)s, \
                        last_login_datetime = %(last_login_datetime)s \
                    WHERE \
                        member_idx = %(member_idx)s'
            param = {
                'login_token': loginToken,
                'last_login_datetime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),
                'member_idx': member['member_idx'],
            }
            self.db.execute(query, param)
            self.db.commit()
            return loginToken
        except Exception as e:
            return e

    def tokenValidation(self, request):
        try:
            query = 'SELECT \
                        COUNT(*) AS cnt \
                    FROM \
                        Member \
                    WHERE \
                        member_idx = %(member_idx)s \
                        AND login_token = %(login_token)s'
            param = {
                'member_idx': request['member_idx'],
                'login_token': request['login_token']
            }
            result = self.db.executeOne(query, param)
            return result['cnt']
        except Exception as e:
            return e

    def tokenDelete(self, member_idx):
        try:
            query = 'UPDATE `Member` SET \
                        login_token = %(login_token)s \
                    WHERE \
                        member_idx = %(member_idx)s'
            param = {
                'login_token': '',
                'member_idx': member_idx,
            }
            self.db.execute(query, param)
            self.db.commit()
            return True
        except Exception as e:
            return e
