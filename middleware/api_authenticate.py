from flask import request, abort
import pymysql, os
from dotenv import load_dotenv

load_dotenv()

class ApiAuthenticate:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if str(environ['HTTP_AUTHORIZATION']) != str('Bearer ' + os.getenv('API_KEY')):
            environ['HTTP_AUTHORIZATION'] = ''
        return self.app(environ, start_response)