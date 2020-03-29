import pickle
import os

import pandas as pd
from sklearn import model_selection
from sklearn.neural_network import MLPClassifier


def model_fitting(x, y, test_size=0.33, seed=7, pfi_fitted_models=''):
    """ Save the model fitted on the input data """

    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=test_size, random_state=seed)

    model = MLPClassifier()
    model.fit(x_train, y_train)

    if not os.path.exists(pfi_fitted_models):
        raise ValueError()

    pickle.dump(model.get_params(), open(pfi_fitted_models, 'wb'))

    scored_model_assessment = model.score(x_test, y_test)

    return scored_model_assessment


def apply_model(pfi_fitted_models, x):
    """ apply a fitted model whose parameters are saved in the given file """
    model_params = pickle.load(open(pfi_fitted_models, 'rb'))
    model = MLPClassifier()
    model.set_params(**model_params)
    y = model.predict(x)
    model.predict_proba(x)
    return y


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(__file__))
    # access to CSV in the other repo, in the future access via DB
    data_folder = os.path.join(root, "data_simulator", "data_new")

    assert os.path.exists(data_folder), data_folder

    pfi_patients_list = os.path.join(data_folder, "patients_list.csv")
    pfi_patients_data = os.path.join(data_folder, "measurements.csv")

    assert os.path.exists(pfi_patients_list), pfi_patients_list
    assert os.path.exists(pfi_patients_data), pfi_patients_data

    patients_list_df = pd.read_csv(pfi_patients_list, index_col=0)
    patients_data_df = pd.read_csv(pfi_patients_data, index_col=0)

    # first filter: for each patient get a table like

    # second filter: reduce the history to an array of parameters with the trend

    # split into a balanced dataset

    # train

    # test
