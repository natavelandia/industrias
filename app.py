from flask import Flask, request, render_template
import os
import requests, json
import numpy as np
import pickle
import joblib

from flask import Flask,render_template
from sklearn.linear_model import Ridge
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.decomposition import PCA  
from flask import Flask, render_template, request, session

app= Flask (__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        aroma = request.form['aroma']
        sabor = request.form['sabor']
        regusto = request.form['regusto']
        acidez = request.form['acidez']
        cuerpo = request.form['cuerpo']
        balance = request.form['balance']
        general = request.form['general']
        #'Aroma', 'Flavor', 'Aftertaste', 'Acidity', 'Body', 'Balance', 'Overall'
        


        




        return render_template('index.html', feature=aroma, puntaje=aroma)

    return render_template('index.html')

if __name__=="__main__":

    app.run(debug=True)
