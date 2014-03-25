from flask import Flask, session, render_template, request, redirect, url_for


app = Flask(__name__)

app.secret_key = "wrluwvlwrnmnlqewrpqwreoghclvkjfn"

@app.route("/")
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.debug = True;
    app.run()
