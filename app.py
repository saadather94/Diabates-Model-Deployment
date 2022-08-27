import re
from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/Home')
def home():
    return render_template("home.html")

@app.route('/sub', methods=['POST'])
def submit():
    if request.method == 'POST':
        Preg= request.form["preg"]
        Plgluco= request.form["plgluco"]
        Trithk= request.form["Trithk"]
        Insuline= request.form["insuline"]
        Bmi= request.form["bmi"]
        Diapedgr= request.form["diapedgrs"]
        Age= request.form["age"]
        DistolicBP= request.form["distolicBP"]

        pred = model.get_pred(Preg,Plgluco,DistolicBP,Trithk,Insuline,Bmi,Diapedgr,Age)
        if(pred == 0):
            prd = 'Non Diabetic'
        else:
            prd = 'Diabetic'    

    return render_template("sub.html", prediction = prd )


if __name__ == '__main__':
    app.run(debug=True)