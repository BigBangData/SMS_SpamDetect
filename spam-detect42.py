#!/usr/bin/env python
import os
import joblib
import numpy as np

import custom.deploy_models as deploy
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict_spam():

    XGboost_mod1_PATH = os.path.join("data",
                                     "5_deployment",
                                     "XGboost_mod1.joblib")

    with open(XGboost_mod1_PATH, 'rb') as f:
        XGboost_model = joblib.load(f)

    if request.method == 'POST':

        msg = request.form['message']
        text = np.array([msg])

        try:
            (counter
            , vocabulary
            , bot
            , ziparrays # vocab, bot, and tfidf
            , svd
            , cossim
            , X_processed) = deploy.transform_newdata(text)
            y_pred = XGboost_model.predict(X_processed)
        except Exception as e:
            raise e

    return render_template('result.html'
                          , prediction = y_pred[0]
                          , counter =  counter
                          , vocabulary = vocabulary
                          , bot = bot
                          , ziparrays = ziparrays
                          , svd = svd
                          , cossim = cossim)
if __name__=='__main__':
    #app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=80)
