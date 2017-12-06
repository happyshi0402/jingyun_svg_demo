from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("svg_edit.html")


if __name__ == '__main__':
    print "http://localhost:5101"
    app.run(host="0.0.0.0", port=5101)
