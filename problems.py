# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
import rampwf as rw
from sklearn.model_selection import train_test_split
from datetime import timedelta

problem_title = 'Prediction of the filling of Velib stations'
_target_column_name = 'filling'
_prediction_label_names = [0, 1, 2] 
#'0' if the number of bike available is less than min(2, 10% number of docks) 
#'2' if the number of dock available is less than min(1, 5% number of docks)
#'1' is station filled okay
# A type (class) which will be used to create wrapper objects for y_pred
Predictions = rw.prediction_types.make_multiclass(
    label_names=_prediction_label_names)

# An object implementing the workflow
workflow = rw.workflows.FeatureExtractorClassifier()

#no soft score matrix

#no tf score matrix

score_types = [
    rw.score_types.Accuracy(name='acc', precision=3),
]
#choice of score_type : Accuracy

def get_cv(X, y):
    """Slice folds by equal date intervals."""
    date = pd.to_datetime(X['date'])
    n_days = (date.max() - date.min()).days
    n_splits = 8
    fold_length = n_days // n_splits
    fold_dates = [date.min() + timedelta(days=i * fold_length)
                  for i in range(n_splits + 1)]
    for i in range(n_splits):
        test_is = (date >= fold_dates[i]) & (date < fold_dates[i + 1])
        test_is = test_is.values
        train_is = ~test_is
        yield np.arange(len(date))[train_is], np.arange(len(date))[test_is]


def _read_data(path, f_name):
    data = pd.read_csv(os.path.join(path, 'data', f_name), sep='\t')
    y_array = data[_target_column_name].values
    X_df = data.drop(_target_column_name, axis=1)
    test = os.getenv('RAMP_TEST_MODE', 0)
    if test:
        return X_df[:100], y_array[:100]
    else:
        return X_df, y_array


def get_train_data(path='.'):
    f_name = 'train.csv'
    return _read_data(path, f_name)


def get_test_data(path='.'):
    f_name = 'test.csv'
return _read_data(path, f_name)
