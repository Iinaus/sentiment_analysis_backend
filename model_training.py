import pandas as pd
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

def train_model():

    # Check if the model is already cached
    try:
        # Attempt to load the model from the file
        model = load('sentiment_model.joblib')
        print("Loaded cached model.")

    except FileNotFoundError:   
        print("Training new model...")

        # Load the training data from a CSV file
        df = pd.read_csv('train.csv', encoding='latin1')

        # Remove missing values in the dataset
        df.dropna(inplace=True)

        # Define the input features (X) and target variable (y)
        x = df['selected_text']
        y = df['sentiment']

        # Split the data into training and test sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.01, random_state=42)

        # Create a machine learning pipeline
        text_clf = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', LinearSVC())
        ])

        # Train the model using the training data
        text_clf.fit(x_train, y_train)

        # Save the trained model for later use
        dump(text_clf, 'sentiment_model.joblib')

        model = text_clf

    return model