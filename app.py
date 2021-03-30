from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/kyuuyo")
def kyuuyo():
    kyuuyo = request.args.get("kyuuyo")
    return render_template("kyuuyo.html", kyuuyo=kyuuyo)

@app.route("/kyuuyoanswer")
def kyuuyoanswer():
    return render_template("kyuuyoanswer.html")


@app.route("/enn")
def enn():
    en = request.args.get("en")
    return render_template("enn.html", en=en)

@app.route("/ennanswer")
def ennanswer():
    return render_template("ennanswer.html")

if __name__ == "__main__":
    app.run(debug=True)