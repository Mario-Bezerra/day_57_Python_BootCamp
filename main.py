from flask import Flask, render_template
import requests
from post import Post


url = "https://api.npoint.io/4af156202f984d3464c3"
response = requests.get(url)
all_blogs = response.json()
blog_objects = []
for blog in all_blogs:
    b_object = Post(blog["id"], blog["title"], blog["subtitle"], blog["body"])
    blog_objects.append(b_object)

app = Flask(__name__)

@app.route('/')
def blog():
    return render_template("index.html", blog_objects=blog_objects)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in blog_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
