from flask import Flask , render_template , request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/random" , methods=["GET"])
def get_random_cafe():
    return "Hello API"

if __name__ == "__main__":
    app.run(debug=True)