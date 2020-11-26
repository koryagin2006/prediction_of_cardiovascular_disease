from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from requests.exceptions import ConnectionError
from wtforms import IntegerField, SelectField, StringField
from wtforms.validators import DataRequired

import urllib.request
import json


class ClientDataForm(FlaskForm):
    # description = StringField('Job Description', validators=[DataRequired()])
    # company_profile = StringField('Company Profile', validators=[DataRequired()])
    # benefits = StringField('Benefits', validators=[DataRequired()])
    age = StringField('age', validators=[DataRequired()])
    gender = StringField('gender', validators=[DataRequired()])
    height = StringField('height', validators=[DataRequired()])
    weight = StringField('weight', validators=[DataRequired()])
    ap_hi = StringField('ap_hi', validators=[DataRequired()])
    ap_lo = StringField('ap_lo', validators=[DataRequired()])
    smoke = StringField('smoke', validators=[DataRequired()])
    alco = StringField('alco', validators=[DataRequired()])
    active = StringField('active', validators=[DataRequired()])


app = Flask(__name__)
app.config.update(
    CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess',
)


def get_prediction(
        age, gender, height, weight, ap_hi, ap_lo, smoke, alco, active,
        description, company_profile, benefits
):
    body = {
        'age': age,
        'gender': gender,
        'height': height,
        'weight': weight,
        'ap_hi': ap_hi,
        'ap_lo': ap_lo,
        'smoke': smoke,
        'alco': alco,
        'active': active,
        # 'description': description,
        # 'company_profile': company_profile,
        # 'benefits': benefits
    }

    myurl = "http://0.0.0.0:8180/predict"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    # print (jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
    return json.loads(response.read())['predictions']


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predicted/<response>')
def predicted(response):
    response = json.loads(response)
    print(response)
    return render_template('predicted.html', response=response)


@app.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    form = ClientDataForm()
    data = dict()
    if request.method == 'POST':
        # data['description'] = request.form.get('description')
        # data['company_profile'] = request.form.get('company_profile')
        # data['benefits'] = request.form.get('benefits')
        data['age'] = request.form.get('age')
        data['gender'] = request.form.get('gender')
        data['height'] = request.form.get('height')
        data['weight'] = request.form.get('weight')
        data['ap_hi'] = request.form.get('ap_hi')
        data['ap_lo'] = request.form.get('ap_lo')
        data['smoke'] = request.form.get('smoke')
        data['alco'] = request.form.get('alco')
        data['active'] = request.form.get('active')

        try:
            response = str(get_prediction(
                # data['description'],
                # data['company_profile'],
                # data['benefits'],
                data['age'],
                data['gender'],
                data['height'],
                data['weight'],
                data['ap_hi'],
                data['ap_lo'],
                data['smoke'],
                data['alco'],
                data['active'],
            ))
            print(response)
        except ConnectionError:
            response = json.dumps({"error": "ConnectionError"})
        return redirect(url_for('predicted', response=response))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)
