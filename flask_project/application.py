import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from flask import Flask,request,jsonify,render_template


application = Flask(__name__)
app=application

## import ridge regressor and Standard Scaler
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method== "POST":
         Temperature= float(request.form['Temperature'])
         RH = float(request.form['RH'])
         Ws = float(request.form['Ws'])
         Rain = float(request.form['Rain'])
         FFMC = float(request.form['FFMC'])
         DMC= float(request.form['DMC'])
         ISI = float(request.form['ISI'])
         Region = request.form['Region']
         Classes = request.form['Classes']

         new_data_sacled=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Region,Classes]])
         result=ridge_model.predict(new_data_sacled)

         return render_template('home.html',results=result[0])         
    else:
        return render_template('home.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0")