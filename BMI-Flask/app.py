from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = round(weight / (height ** 2), 2)
        bmi_category = get_bmi_category(bmi)
        return render_template('index.html', bmi=bmi, bmi_category=bmi_category)
    else:
        return render_template('index.html')

def get_bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

if __name__ == '__main__':
    app.run(debug=True)
