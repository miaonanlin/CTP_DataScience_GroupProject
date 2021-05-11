import flask
import os
import pickle
import pandas as pd
from skimage import io
from skimage import transform

app = flask.Flask(__name__, template_folder='templates')


path_to_classifier = 'model/classifier.pkl'
with open(path_to_classifier, 'rb') as f:
    model = pickle.load(f)



@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('mainpage.html'))

    #if flask.request.method == 'POST':
        # Get the input from the user.
        #user_input_text = flask.request.form["input_variable_one","another-input-variable",
         #"third-input-variable", "fourth-input-variable", "fifth-input-variable",
        #"sixth-input-variable", "seventh-input-variable", 'eighth-input-variable',
        #"ninth-input-variable", "tenth-input-variable"]

        if flask.request.method == 'POST':
            # Get the input from the user.
            var_one = flask.request.form['input_variable_one']
            var_two = flask.request.form['another-input-variable']
            var_three = flask.request.form['third-input-variable']
            var_fourth = flask.request.form['fourth-input-variable']
            var_fifth = flask.request.form['fifth-input-variable']

            var_sixth = flask.request.form['sixth-input-variable']
            var_seventh = flask.request.form['seventh-input-variable']
            var_eighth = flask.request.form['eighth-input-variable']
            var_ninth = flask.request.form['ninth-input-variable']
            var_tenth = flask.request.form['tenth-input-variable']

        user_input_text = [var_one, var_two, var_three, var_fourth, var_fifth,
                         var_sixth, var_seventh, var_eighth, var_ninth, var_tenth]

        X = user_input_text

        # Make a prediction
        predictions = model.predict(X)

        # Get the first and only value of the prediction.
        prediction = predictions[0]

        # Get the predicted probabs
        predicted_probas = model.predict_proba(X)

        # Get the value of the first, and only, predicted proba.
        predicted_proba = predicted_probas[0]


        precent_legit = predicted_proba[0]
        precent_phisihing = predicted_proba[1]


        return flask.render_template('mainpage.html',
            input_text=user_input_text,
            result=prediction,
            precent_legit=precent_legit,
            precent_phisihing=precent_phisihing)



    return(flask.render_template('mainpage.html'))





if __name__ == '__main__':
    app.run(debug=True)
