from flask import Flask , render_template
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.datetime.now()
    today = today.strftime("%Y")

    return render_template('index.html' , curr_date = today )

@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/5c96c8cd8f1a01484bd7"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html' , posts = all_posts)

# @app.route('/guess/<user_name>')
# def create_data(user_name):
#     AGE_URL = "https://api.agify.io"
#     GENDER_URL = "https://api.genderize.io" 

#     age_response = requests.get(AGE_URL, params={"name": user_name})
#     gender_response = requests.get(GENDER_URL, params={"name": user_name})

#     name_age = age_response.json()["age"]
#     name_gender = gender_response.json()["gender"]

#     return render_template('index.html' , age = name_age , gender = name_gender , name = user_name )


if __name__ == '__main__':
    app.run(debug=True)   