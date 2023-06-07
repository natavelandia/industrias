from flask import Flask, request, render_template
import os
import requests, json
import numpy as np
import pickle


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
        with open('ridge.pkl', 'rb') as archivo:
            modelo = pickle.load(archivo)
        with open('scaler.pkl', 'rb') as archivo:
            scalar = pickle.load(archivo)
        with open('pca.pkl', 'rb') as archivo:
            pca = pickle.load(archivo)

        feature=np.asarray([aroma,sabor,regusto,acidez,cuerpo,balance,general])
        # con 8.58,8.50,8.42,8.58,8.25,8.42,8.58 da 89.33
        feat_html=feature
        feature=feature.reshape(1, -1)
        print(feature.shape)
        scaler = scalar.transform(feature)
        pc = pca.transform(scaler)
        prediction = np.round(modelo.predict(pc),2)

        




        return render_template('index.html', feature=feat_html, puntaje=prediction)

    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
