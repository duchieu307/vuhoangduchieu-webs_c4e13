from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route("/ketqua")
def ketqua():
    return render_template("result.html")

@app.route("/dangky")
def dangky():
    return render_template("register.html")

@app.route('/trangchu')
def trangchu():
    return render_template("map.html")

if __name__ == '__main__':
  app.run(debug=True)
