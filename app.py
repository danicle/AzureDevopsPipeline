from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)


filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
x_columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']


@app.route("/")
def home():
    return render_template('hello_there.html')


@app.route("/predict", methods=['POST'])
def predict():

    print(request.form.values())
    features = np.array([float(x) for x in request.form.values()]).reshape(1,-1)
    features = pd.DataFrame(features, columns = x_columns)
    preds = loaded_model.predict(features)[0]
    preds = round(preds,2)
    return render_template("hello_there.html", output = 'predict is: {}'.format(preds))


if __name__ == "__main__":
    app.run(debug=True, port= 5042)