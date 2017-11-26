from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<weight>/<height>')
def index(weight, height):
    weight = int(weight)
    height = float(height)
    BMI = weight/ (height*2)
    answer = 'HeHe'
    if BMI < 16 :
        answer = "Severely Underweight"
    elif BMI < 18.5 :
        answer = "Underweight"
    elif BMI < 25 :
        answer = "Normal"
    elif BMI < 30 :
        answer = "Overweight"
    else :
        answer = "Obese"
    return str(BMI) + " " +answer

if __name__ == '__main__':
  app.run(debug=True)
