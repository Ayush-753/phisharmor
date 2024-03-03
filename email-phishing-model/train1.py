import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
df = pd.read_csv('mail_data.csv')
data = df.where((pd.notnull(df)), '')
X = data['Message']
Y = data['Category']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state = 3)
feature_extraction = TfidfVectorizer(min_df = 1, stop_words = 'english', lowercase = True)

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')
model = LogisticRegression()
prediction_on_training_data = model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)

prediction_on_test_data = model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test, prediction_on_test_data)
input_your_mail = ["Double your mins & txts on Orange or 1/2 price linerental - Motorola and SonyEricsson with B/Tooth FREE-Nokia FREE Call MobileUpd8 on 08000839402 or2optout/HV9D"]

input_data_features = feature_extraction.transform(input_your_mail)

prediction = model.predict(input_data_features)

print(prediction)

if(prediction[0]==1):
    print('Ham Mail')
    
else:
    print('Spam Mail')

# Detect ham or spam for more new emails
new_emails_to_detect = ["Flights from ₹1,799 Making new-year travel resolutions"]

# Ensure all elements in the list are valid strings
new_emails_to_detect = [str(email) for email in new_emails_to_detect]

# Alternatively, if you have the original vectorizer instance:
loaded_vectorizer = feature_extraction

# Use the same vectorizer that was fit during training
feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
X_train_features = feature_extraction.fit_transform(X_train)

# Transform the new emails using the original vectorizer
new_email_features_to_detect = feature_extraction.transform(new_emails_to_detect)

# Check the number of features in the new data
print(new_email_features_to_detect.shape)

# Make predictions on the new emails
predictions_to_detect = model.predict(new_email_features_to_detect)

# Print predictions for new emails
print(predictions_to_detect)

# Print results based on predictions for new emails
for pred in predictions_to_detect:
    if pred == 1:
        print('Ham Mail')
    else:
        print('Spam Mail')