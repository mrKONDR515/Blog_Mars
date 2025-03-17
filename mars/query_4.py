from flask import Flask
from data.db_session import create_session, global_init
from data.users import User
from data.jobs import Jobs
from sqlalchemy import or_

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# ##### Это надо отправить -- начало{
def main():
    global_init(input())

    session = create_session()

    for user in session.query(User).filter(or_(User.position.like("%chief%"), User.position.like("%middle%"))):
        print(user, user.position)


if __name__ == '__main__':
    main()
# ##### Это надо отправить -- конец}