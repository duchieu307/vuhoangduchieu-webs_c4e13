from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Hello'
@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/school')
def school():
    return redirect("http://techkids.vn/", code = 302)


if __name__ == '__main__':
  app.run(debug=True)
