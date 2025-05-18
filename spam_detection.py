import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

# Read data with correct path
data = pd.read_csv(r"c:\Users\pc\OneDrive\Desktop\spam\spam.csv")

# Data preprocessing
data.drop_duplicates(inplace=True)
data['Category'] = data['Category'].replace(['ham','spam'],['Not Spam','Spam'])

mess = data['Message']
cat = data['Category']

# Split data with random_state for reproducibility
(mess_train,mess_test,cat_train,cat_test) = train_test_split(mess, cat, test_size=0.2, random_state=42)

# Text vectorization
cv = CountVectorizer(stop_words='english')
features = cv.fit_transform(mess_train)

# Model training
model = MultinomialNB()
model.fit(features, cat_train)

# Model evaluation
features_test = cv.transform(mess_test)
accuracy = model.score(features_test,cat_test)

def predict(message):
    input_message = cv.transform([message]).toarray()
    result = model.predict(input_message)
    return result[0]  # Return single prediction instead of array

# Streamlit UI
st.header('Spam Detection')
st.write(f'Model Accuracy: {accuracy:.2%}')

input_mess = st.text_input('Enter Message Here')

if st.button('Validate'):
    if input_mess:  # Check if input is not empty
        output = predict(input_mess)
        st.write(f'Prediction: {output}')
    else:
        st.warning('Please enter a message to classify')