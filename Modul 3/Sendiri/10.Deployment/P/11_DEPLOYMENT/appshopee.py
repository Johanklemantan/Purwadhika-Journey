from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# halaman home
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    return render_template('predictshopee.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method=='POST':
        input = request.form

        df_to_predict = pd.DataFrame({
            'age': [input['age']],
            'domain': [input['domain']],
            'country': [input['country']],
            'day': [input['day']],
            'character_length': [input['character_length']],
            'last_time_open_email': [input['last_time_open_email']],
            'last_time_open_shopee': [input['last_time_open_shopee']],
            'last_time_checkout_shopee': [input['last_time_checkout_shopee']],
            'open_frequency': [input['open_frequency']],
            'login_frequency': [input['login_frequency']],
            'checkout_frequency': [input['checkout_frequency']]
        })

        prediksi = model.predict_proba(df_to_predict)[:,1]

        if prediksi > 0.84:
            results = 'Read the Promotion Email'
        else:
            results = 'Not Read the Promotion Email'

        return render_template('resultshopee.html', data=input, pred=results)

if __name__ == '__main__':
    
    filename = 'logit_final.sav'
    model = pickle.load(open(filename,'rb'))

    app.run(debug=True)