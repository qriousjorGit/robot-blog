from flask import Flask, render_template, request
from post import Post
import requests

BLOG_API = "https://api.npoint.io/4af156202f984d3464c3"
blog_data = requests.get(BLOG_API).json()

blog_objects = []

for blogs in blog_data:
    post = Post(post_id=blogs["id"], body=blogs["body"], title=blogs["title"], subtitle=blogs["subtitle"])
    blog_objects.append(post)

app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("index.html", all_posts=blog_objects)

@app.route('/form')
def show_form():
    return render_template("form.html")

@app.route("/login", methods=["POST"])
def login():
    user = request.form["username"]
    pword = request.form["password"]
    return render_template("login.html", username=user, password=pword)


# @app.route("/<int:index>")
# def show_post(index):
#     requested_post = None
#     for blog in blog_objects:
#         if index == blog.id:
#             requested_post = blog
#     return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
