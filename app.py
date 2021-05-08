import flask
import os
import pickle
import pandas as pd
from skimage import io
from skimage import transform

app = flask.Flask(__name__, template_folder='templates')

#path_to_vectorizer = 'models/vectorizer.pkl'
path_to_classifier = 'models/classifier.pkl'
#path_to_image_classifier = 'models/image-classifier.pkl'

#with open(path_to_vectorizer, 'rb') as f:
    #vectorizer = pickle.load(f)

with open(path_to_classifier, 'rb') as f:
    model = pickle.load(f)

#with open(path_to_image_classifier, 'rb') as f:
    #image_classifier = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('index.html'))



@app.route('/input_values/', methods=['GET', 'POST'])
def input_values():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('input_values.html'))

    if flask.request.method == 'POST':
        # Get the input from the user.
        var_one = flask.request.form['input_variable_one']
        var_two = flask.request.form['another-input-variable']
        var_three = flask.request.form['third-input-variable']

        list_of_inputs = [var_one, var_two, var_three]

        return(flask.render_template('input_values.html',
            returned_var_one=var_one,
            returned_var_two=var_two,
            returned_var_three=var_three,
            returned_list=list_of_inputs))

    return(flask.render_template('input_values.html'))




if __name__ == '__main__':
    app.run(debug=True)
