import time
from flask import Flask

app = Flask(__name__)

# html elements decorators
def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper
def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper
def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

#different routes using the app.route decorator
@app.route('/')
def index():
    return '<h1>Hello User!</h1>' \
            '<p> This is a paragraph </p>' \
            '<iframe src="https://giphy.com/embed/h4sIGoW7qd9lJl5jze" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/bbcamerica-nature-bbc-america-seven-worlds-one-planet-h4sIGoW7qd9lJl5jze">via GIPHY</a></p>'
@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Goodbye'

#Creating variable paths and converting the path to a specific data type
@app.route('/username/<name>/<int:number>')
def user(name,number):
    return f'Hello {name} your age is {number}'


if __name__ == '__main__':
    app.run(debug=True)