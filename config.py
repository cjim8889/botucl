import os

baseDir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('FLASK_KEY')

class wechatConfig(object):
    token = os.environ.get('WECHAT_KEY') or "G5UeWJtVltORY1fLFHc"
    APP_SECRET = "4490054638a0baee44197a2bd481a429"
    APP_ID = "wx386fcea189bd24c4"

    # TRAP_HTTP_EXCEPTIONS = True
    