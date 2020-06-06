from flask import *
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main_page():
    return render_template("hello.html")

@app.route('/good')
def good():
    name = "Good"
    return name
@app.route('/sex')
def sex():
    message = "Sex"
    return message
@app.route('/kill', methods=["GET"])
def killer():
    return render_template("kill.html")


@app.route('/name', methods=["GET"])
def namepager():
    return render_template("name.html")

if __name__ == "__main__":
    app.run(debug=True)
