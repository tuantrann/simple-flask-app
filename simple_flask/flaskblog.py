from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "author": "Tuan Tran",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2020",
    },
    {
        "author": "Tri Tran",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "January 20, 2021",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)