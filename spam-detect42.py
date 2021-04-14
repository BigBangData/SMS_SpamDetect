#!/usr/bin/env python

# Copyright 2021 Marcelo Sanches
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Attributions
# 
# This Python script was adapted from the original by Chayan Kathuria,
# Data Science and Machine Learning Enthusiast and author at 
# towardsdatascience.com. See original Medium post:
# https://towardsdatascience.com/build-deploy-a-spam-classifier-app-on-heroku-cloud-in-10-minutes-f9347b27ff72

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