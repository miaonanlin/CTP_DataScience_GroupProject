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

        user_input = [var_one, var_two, var_three, var_fourth, var_fifth,
                    var_sixth, var_seventh, var_eighth, var_ninth, var_tenth]

        features = ["SSL Final State", "URL of Anchor", "Web Traffic", "Having Sub Domain", 
                    "Links in Tags", "Prefix Suffix", "Links Pointing to Page", "SFH", 
                    "Request URL", "Domain Registeration Length"]

        for i in range(10):

            user_input_text[i] = features[i] + ": " + user_input_text[i]

        for i in range(10):

            if (user_input[i] == "Legitimate"):

                user_input[i] = "1"

            elif (user_input[i] == "Suspicious"):

                user_input[i] = "0"

            elif (user_input[i] == "Phishing"):

                user_input[i] = "-1"

            user_input[i] = int(user_input[i])

        X = user_input

        X = np.array(X)

        X = X.reshape(1, -1)

        X = X.tolist()

        # Make a prediction
        predictions = model.predict(X)

        # Get the first and only value of the prediction.
        prediction = predictions[0]

        prediction = str(prediction)

        if (prediction == "1"):

            prediction = "Legitimate Website"

        if (prediction == "-1"):

            prediction = "Phishing Website"

        # Get the predicted probabs
        predicted_probas = model.predict_proba(X)

        # Get the value of the first, and only, predicted proba.
        predicted_proba = predicted_probas[0]


        percent_legit = predicted_proba[1] * 100
        percent_phishing = predicted_proba[0] * 100

#        labels = ["Legitimate", "Phishing"]

#        values = [percent_legit, percent_phishing]

#        colors = ["#ABCABC", "#46BFBD"]

        data = {"Legitimate" : percent_legit, "Phishing" : percent_phishing}

        return flask.render_template('mainpage.html',
            input_text = user_input_text,
            result = prediction,
            percent_legit = percent_legit,
            percent_phishing = percent_phishing,
            data = data)

    return(flask.render_template('mainpage.html'))


@app.route('/about/')
def about():
    return flask.render_template('about.html')

@app.route('/info/')
def info():
    return flask.render_template('info.html')



if __name__ == '__main__':
    app.run(debug=True)
