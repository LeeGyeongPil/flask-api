
from flask_inputs import Inputs
from wtforms.validators import *

# 로그인 유효성 검사
class LoginValidation(Inputs):
    form = {
        'id': [InputRequired(), Length(max=10)],
        'password': [InputRequired()],
    }

# 로그아웃 유효성 검사
class LogoutValidation(Inputs):
    form = {
        'member_idx': [InputRequired()],
        'login_token': [InputRequired()],
    }

# 회원가입 유효성 검사
class JoinValidation(Inputs):
    form = {
        'id': [InputRequired(), Regexp(r'^[a-zA-Z0-9]*$'), Length(max=20)],
        'name': [InputRequired(), Regexp(r'^[가-힣a-zA-Z]*$'), Length(max=20)],
        'nick': [InputRequired(), Regexp(r'^[a-z]*$'), Length(max=30)],
        'password': [InputRequired(), Regexp(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'), Length(min=10)],
        'tel': [InputRequired(), Regexp(r'^[0-9]*$'), Length(max=13)],
        'email': [InputRequired(), Email(), Length(max=100)],
        'gender': [Optional(), Regexp(r'^[MF]$')],
    }