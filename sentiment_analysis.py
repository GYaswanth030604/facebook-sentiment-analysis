import pandas as pd
import nltk
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

nltk.download('stopwords')
from nltk.corpus import stopwords

# Load dataset
data = pd.read_csv("dataset.csv")

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = "".join([char for char in text if char not in string.punctuation])
    return text

data['clean_text'] = data['comment'].apply(clean_text)

# Feature extraction
vectorizer = CountVectorizer(stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(data['clean_text'])
y = data['sentiment']

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

# Test example
sample = ["This product is amazing"]
sample_vec = vectorizer.transform(sample)
print("Prediction:", model.predict(sample_vec))
