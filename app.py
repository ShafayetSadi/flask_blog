from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        "author": "Shafayet Sadi",
        "title": "Hello Word",
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

if __name__ == '__main__':
    app.run(debug=True)