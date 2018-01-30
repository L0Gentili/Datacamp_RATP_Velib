# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import string

class FeatureExtractor:

    def fit(self, X_df, y=None):
        """
        ----------
        X_df : pandas.DataFrame
        """
        data['capacity'] = data['numBikesAvailable'] + data['numDocksAvailable'] #complete the capacity of each station
        data = data[data['capacity'] != 0] #removal of station with capacity listed as 0
        X_df = X_df.fillna(0)
        return self

    def fit_transform(self, X_df, y=None):
        return self.fit(X_df).transform(X_df)

    def transform(self, X_df):
        return X
      
