from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/kinoteatr.db")
    
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == 2).one()
    print(user.name)
##    app.run()


if __name__ == '__main__':
    main()
