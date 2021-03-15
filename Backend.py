#Initialising variables
model = None
x_train = None
x_test = None
y_train = None
y_test = None
session = 0
features = None


#Necessary imports
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import tensorflow as tf
from tensorflow import keras
import joblib
import os
from keras.models import model_from_json
from keras.models import model_from_yaml

#Loading various types of model and dataset
def to_dataframe(from_data, filename):
    to_data = None
    if '.pkl' in filename:
        to_data = joblib.load(from_data)
    elif ".csv" in filename:
        to_data = pd.read_csv(from_data)
    elif ".json" in filename:
        to_data = pd.read_json(from_data)
    return to_data


def convert(mod, filename):
    model = None
    if not(os.path.exists(mod)):
        return "Model does not exist"
    if os.path.isfile(mod):
        model = isFile(mod, filename)
    if os.path.isdir(mod):
        model = isDir(mod, filename)
    return model
        

def isFile(mod, filename):
    model = None
    _, end = os.path.splitext(filename)
    if (".h5" in filename):
        model = keras.models.load_model(mod)
    if (end == '.pkl'):
        model = joblib.load(mod)
    if (".yaml" in filename):
        file = open(mod, "r")
        model = model_from_yaml(file.read())
        file.close()
    if (".json" in filename):
        file = open(mod, "r")
        model = model_from_json(file.read())
        file.close()
    return model

def isDir(mod, filename):
    files = os.listdir(mod)
    for x in files:
        if x.endswith(".pb"):
            model = keras.models.load_model(mod)
            return model

#Explanation function
import anvil.media
@anvil.server.callable
def returnWeb():
    global session
    from interpret.ext.blackbox import TabularExplainer
    if features != None:
        explainer = TabularExplainer(model, x_train, features=features)
    else:
        explainer = TabularExplainer(model, x_train)
    global_explanation = explainer.explain_global(x_test)
    from interpret_community.widget import ExplanationDashboard
    ExplanationDashboard(global_explanation, model, datasetX=x_test, true_y=y_test, port=80)
    session += 1
    return ("http://localhost:80/"+str(session))


#Web app's upload functions
import anvil.media
@anvil.server.callable
def uploadModel(file, filename):
    import joblib
    import os
    import tensorflow
    from tensorflow import keras
    global model
    with anvil.media.TempFile(file) as file_path:
        model = convert(file_path, filename)
        return [file, filename]


import anvil.media
@anvil.server.callable
def uploadX_test(file, filename):
    import joblib
    global x_test
    with anvil.media.TempFile(file) as file_path:
        x_test = to_dataframe(file_path, filename)
    return [file, filename]

import anvil.media
@anvil.server.callable
def uploadX_train(file, filename):
    import joblib
    global x_train
    with anvil.media.TempFile(file) as file_path:
        x_train = to_dataframe(file_path, filename)
        return [file, filename]

import anvil.media
@anvil.server.callable
def uploadY_test(file, filename):
    import joblib
    global y_test
    with anvil.media.TempFile(file) as file_path:
        y_test = to_dataframe(file_path, filename)
    return [file, filename]

import anvil.media
@anvil.server.callable
def uploadY_train(file, filename):
    import joblib
    global y_train
    with anvil.media.TempFile(file) as file_path:
        y_train = to_dataframe(file_path, filename)
    return [file, filename]

import anvil.media
@anvil.server.callable
def uploadLabels():
    global dataLabels
    return [model]

#Extra web app functions
@anvil.server.callable
def clearVars():
    global model
    model = None
    global x_train 
    x_train = None
    global x_test
    x_test = None
    global y_train
    y_train = None
    global y_test
    y_test = None
    global features
    features = None


@anvil.server.callable
def printVars():
    return [x_train, x_test, y_train, y_test]


@anvil.server.callable
def setFeatures(string):
    global features
    features = string.split(", ")
    return features


@anvil.server.callable
def resetFeatures():
    global features
    features = None



#Running computer as server and uplinking to web app
import anvil.server

anvil.server.connect("36PAL3JXQZYASJTZZTBEPWVB-4QNLE2RQGTTX3TET")

anvil.server.wait_forever()
