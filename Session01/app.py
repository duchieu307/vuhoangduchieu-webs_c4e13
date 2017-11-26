from flask import Flask, render_template
app = Flask(__name__)


# @app.route('/')
# def index():
#     return "Hello World"
#
#
# @app.route('/hello-me')
# def hello_me():
#     return "Hello Hello"
#
# @app.route('/<name>/<firstname>')
# def hello(name, firstname):
#     return 'Hello' + name + firstname
#
# @app.route('/sum/<int:x>/<int:y>')
# def sum(x, y):
#
#     return str(x + y)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
