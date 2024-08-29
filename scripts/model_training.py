import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def train_model(data_path):
    df = pd.read_csv(data_path)
    X = df[['Rain Fall (mm)', 'Fertilizer', 'Temperatue', 'Nitrogen (N)', 'Phosphorus (P)', 'Potassium (K)']]
    y = df['Yeild (Q/acre)']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print('Mean Squared Error:', mse)
    print('R-squared:', r2)

    joblib.dump(model, 'models/crop_yield_model.pkl')

if __name__ == "__main__":
    train_model('data/cleaned_data.csv')
