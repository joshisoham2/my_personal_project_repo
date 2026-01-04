import joblib

model = joblib.load("gb_model.pkl")

def predict(input_df): 
    prediction = model.predict(input_df)
    prediction = str(round(prediction.item(), 2))
    print(type(prediction))
    return prediction