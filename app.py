import flask
import os
import pickle
import pandas as pd
import numpy as np
import sklearn

app = flask.Flask(__name__, template_folder='templates', static_folder='static')


path_to_classifier = 'model/classifier.pkl'
with open(path_to_classifier, 'rb') as f:
    model = pickle.load(f)



@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('mainpage.html'))


    if flask.request.method == 'POST':
            # Get the input from the user.
        var_one = flask.request.form["SSLfinal_State"]
        var_two = flask.request.form["URL_of_Anchor"]
        var_three = flask.request.form["web_traffic"]
        var_fourth = flask.request.form["having_Sub_Domain"]
        var_fifth = flask.request.form["Links_in_tags"]

        var_sixth = flask.request.form["Prefix_Suffix"]
        var_seventh = flask.request.form["Links_pointing_to_page"]
        var_eighth = flask.request.form["SFH"]
        var_ninth = flask.request.form["Request_URL"]
        var_tenth = flask.request.form["Domain_registeration_length"]

        user_input_text = [var_one, var_two, var_three, var_fourth, var_fifth,
                        var_sixth, var_seventh, var_eighth, var_ninth, var_tenth]

        X = user_input_text

        X = np.array(X)

        X = X.reshape(1, -1)

        X = X.tolist()

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
