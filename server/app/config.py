class DefaultConfig(object):
    DB_URL ='localhost:5432'
    DB_NAME = 'testdatabase'
    DB_USER = 'postgres'
    DB_PASSWORD = 'codingisfun29^'

    USER_APP_NAME = 'Web Stocks Login'
    USER_ENABLE_EMAIL = True
    USER_ENABLE_USERNAME = False
    USER_REQUIRE_RETYPE_PASSWORD = False
    USER_LOGOUT_URL = '/sign-out'

    USER_EMAIL_SENDER_EMAIL = 'helpdesk@webstocks.com'

    SECRET_KEY = 'Insecure Development Key asdoincpqoiejrpqoiwejrpqoiejrpqowiejpoimpxozicjzxpcivj'

    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME = 'danieljladner@gmail.com'
    MAIL_PASSWORD = "kjgtlwperueccznq"

    DEBUG=True