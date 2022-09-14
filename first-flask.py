from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():  
    return 'Hello, World !'

@app.route('/bye')
def say_bye():  
    return 'Bye Bye !'

@app.route('/beijing')
def beijing():  
    with open('main.txt' , 'r') as file:
        datat = file.read()
    return datat

if __name__ == "__main__":
    app.run()
