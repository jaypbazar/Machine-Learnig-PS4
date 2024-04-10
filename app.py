from flask import Flask, render_template, url_for, request
import pickle

app = Flask(__name__)

fileObj = open('model.obj', 'rb')
model = pickle.load(fileObj)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        carwidth = float(request.form.get('carwidth'))
        carlength = float(request.form.get('carlength'))
        carheight = float(request.form.get('carheight'))
        enginesize = float(request.form.get('enginesize'))
        horsepower = float(request.form.get('horsepower'))

        predicted_price = model.predict([[carwidth, carlength, carheight, enginesize, horsepower]])
        
        return render_template('index.html', predicted_price = predicted_price)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)