#!/usr/bin/env python
import os
import joblib
import numpy as np

import custom.deploy_models as dp
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
        XGboost_mod1 = joblib.load(f)

    if request.method == 'POST':

        msg = request.form['message']
        txt = np.array([msg])

        try:
            (X_test_counter
            , X_train_transformer_vocab
            , X_test_bot_42
            , X_test_tfidf
            , X_test_svd
            , test_mean_spam_sims
            , X_test_processed
            ) = dp.transform_newdata(txt)
            y_pred = XGboost_mod1.predict(X_test_processed)
        except Exception as e:
            raise e

    return render_template('result.html',
                            prediction = y_pred[0],
                            counter =  dict(X_test_counter[0]),
                            vocabulary = X_train_transformer_vocab,
                            bot = X_test_bot_42
                            )
if __name__=='__main__':
    #app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=80)
