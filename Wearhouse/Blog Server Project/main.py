from flask import Flask, render_template
import requests
from post import Post


blog_url = "https://api.npoint.io/5c96c8cd8f1a01484bd7"
response = requests.get(blog_url)
all_post = response.json()
#all_post = Post(response.json())

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/blog')
def blog():
    return render_template('index.html' , post_list = all_post)
    return render_template('index.html' , post_list = all_post.posts)


@app.route('/post/<int:id>')
def blog_post(id):
    return render_template('post.html' , posts = all_post , post_id = id)

if __name__ == "__main__":
    app.run(debug=True)

