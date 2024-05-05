import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = joblib.load('tfidf_vectorizer.joblib')
nb_model = joblib.load('naive_bayes_model.joblib')
lr_model = joblib.load('logistic_regression_model.joblib')

def analyse_email(email):
    email_tfidf = tfidf_vectorizer.transform(email)
    
    prediction = nb_model.predict(email_tfidf)
    
    if prediction[0] == 1:
        return "Naive Bayes predicts it as Spam"
    else:
        return "Naive Bayes predicts it as Ham"
    
def analyse2_email(email):
    email_tfidf = tfidf_vectorizer.transform(email)
    
    prediction2 = lr_model.predict(email_tfidf)
    
    if prediction2[0] == 1:
        return "Random Forest predicts it as Spam"
    else:
        return "Random Forest predicts it as Ham"
    
def analyse3_email(email):
    email_tfidf = tfidf_vectorizer.transform(email)
    
    prediction2 = lr_model.predict(email_tfidf)
    
    if prediction2[0] == 1:
        return "Logistic regression predicts it as Spam"
    else:
        return "Logistic regression predicts it as Ham"
    
def analyse4_email(email):
    email_tfidf = tfidf_vectorizer.transform(email)
    
    prediction2 = lr_model.predict(email_tfidf)
    
    if prediction2[0] == 1:
        return "Desicion Tree predicts it as Spam"
    else:
        return "Desicion Tree predicts it as Ham"        
        
    
