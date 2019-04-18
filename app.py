from flask import Flask, render_template, url_for, flash, redirect
from forms import ResistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '0270e77bd9e8c8ab55ab4b2cbcccdaeb'

posts = [
    {
        "author": "Shafayet Sadi",
        "title": "Hello World",
        'content': 'My first post.I have written a python program',
        'date': 'April 16, 2019',
    },
    {
        "author": "Sifat Jaman",
        "title": "Hello Hexa Core",
        'content': 'My first post.Welcome to Hexa Core Assylum',
        'date': 'April 16, 2019',
    },
]

@app.route('/')
@app.route('/home')

def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About Page')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = ResistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.user_name.data}!', "success")
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'shafayet.sadi@gmail.com' and form.password.data == '746258':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)