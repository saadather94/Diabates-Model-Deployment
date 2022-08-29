from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import MinMaxScaler
import dia_model

model_pk = pickle.load(open('dia_pred_model.pkl', 'rb'))
app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template("home.html")

@app.route('/Home',methods=['GET'])
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
    
        pred = dia_model.get_pred(Preg,Plgluco,DistolicBP,Trithk,Insuline,Bmi,Diapedgr,Age)
        if(pred == 0):
            prd = 'Non Diabetic'
        else:
            prd = 'Diabetic'    

    return render_template("sub.html", prediction = prd )


if __name__ == '__main__':
    app.run(debug=True)