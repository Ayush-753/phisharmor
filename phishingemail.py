import joblib

def analyse_email(email):
    loaded_model = joblib.load('model.joblib')
    prediction = loaded_model.predict(email)
    prediction = prediction[0]
    return f'The Email is Most Probably a {prediction}'  



