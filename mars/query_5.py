from flask import Flask
from data.db_session import create_session, global_init
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# ##### Это надо отправить -- начало{
def main():
    global_init(input())

    session = create_session()

    for job in session.query(Jobs).filter(max(len(Jobs.collaborators.split(',')))):
        print(job.team_leader)


if __name__ == '__main__':
    main()
# ##### Это надо отправить -- конец}