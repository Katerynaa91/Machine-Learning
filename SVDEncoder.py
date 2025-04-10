#Custom SVD Encoder for Categorical values

import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import OneHotEncoder

class CustomSVDCategoricalEncoder:
    def __init__(self, n_components=2):
        self.n_components = n_components
        self.one_hot_encoder = OneHotEncoder(sparse_output=True)
        self.svd = TruncatedSVD(n_components=self.n_components)

    def fit(self, X, categorical_columns):
        self.categorical_columns = categorical_columns
        # Apply one-hot encoding to categorical columns
        one_hot_encoded = self.one_hot_encoder.fit_transform(X[self.categorical_columns])
        # Fit SVD on the one-hot encoded data
        self.svd.fit(one_hot_encoded)

    def transform(self, X):
        # Apply one-hot encoding to categorical columns
        one_hot_encoded = self.one_hot_encoder.transform(X[self.categorical_columns])
        # Transform using SVD
        svd_transformed = self.svd.transform(one_hot_encoded)
        # Create a DataFrame for the transformed features
        svd_features = pd.DataFrame(svd_transformed, columns=[f'SVD_{col}' for col in self.categorical_columns])#если количество колонок соответствует кол-ву SVD компонентов
                                    # columns=[f'{col}_SVD_{i+1}'for i in range(self.n_components)]) #вариант 2, называет новые колонки по кол-ву SVD компонентов
        # Drop original categorical columns and combine transformed features
        X = X.drop(columns=self.categorical_columns).reset_index(drop=True)
        return pd.concat([X, svd_features], axis=1)

    def fit_transform(self, X, categorical_columns):
        self.fit(X, categorical_columns)
        return self.transform(X)

# Example usage:
data = pd.DataFrame({
    'color': ['red', 'green', 'blue', 'red', 'green'],
    'size': ['small', 'large', 'medium', 'small', 'large'],
    'price': [10, 15, 12, 9, 16]
})

encoder = CustomSVDCategoricalEncoder(n_components=2)
transformed_data = encoder.fit_transform(data, categorical_columns=['color', 'size'])
print(transformed_data)
