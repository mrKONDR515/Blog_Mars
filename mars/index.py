from data.jobs import Jobs
from flask import Flask, render_template, redirect, abort, request
from data import db_session
from data.users import User
from form.user import RegisterForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from form.loginform import LoginForm
from form.jobs import JobsForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    users = db_sess.query(User).all()
    names = {name.id: (name.surname, name.name) for name in users}
    return render_template("index.html", jobs=jobs, names=names)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/jobs',  methods=['GET', 'POST'])
@login_required
def add_jobs():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs()
        job.job = form.title.data
        job.teamleader_id = form.teamleader_id.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.is_finished = form.is_finished.data
        current_user.jobs.append(job)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('jobs.html', title='Adding a job',
                           form=form)


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = JobsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if job:
            if current_user.id == 1 or job.team_leader == current_user.id:
                form.title.data = job.job
                form.teamleader_id.data = job.team_leader
                form.work_size.data = job.work_size
                form.collaborators.data = job.collaborators
                form.is_finished.data = job.is_finished
            else:
                abort(403)
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if job:
            if current_user.id == 1 or job.team_leader == current_user.id:
                job.job = form.title.data
                job.team_leader = form.teamleader_id.data
                job.work_size = form.work_size.data
                job.collaborators = form.collaborators.data
                job.is_finished = form.is_finished.data
                db_sess.commit()
                return redirect('/')
            else:
                abort(403)  # Forbidden
        else:
            abort(404)  # Not Found

    return render_template('jobs.html',
                           title='Editing a work',
                           form=form)


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == id).first()
    if job:
        if current_user.id == 1 or job.team_leader == current_user.id:
            db_sess.delete(job)
            db_sess.commit()
        else:
            abort(403)
    else:
        abort(404)
    return redirect('/')


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()


if __name__ == '__main__':
    main()
