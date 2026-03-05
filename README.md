# Facebook Sentiment Analysis using NLP

## Project Overview
In this project I built a simple sentiment analysis system using Python and Natural Language Processing (NLP).  
The program reads text reviews from a file and analyzes the sentiment of each sentence.  
It determines whether the sentiment expressed in the text is positive, negative, or neutral.

## How the Project Works
The program reads text data from a file called `kindle.txt`.  
Then it processes the text using NLP techniques like tokenization, stemming, lemmatization, and POS tagging.  
After processing the text, the VADER sentiment analysis model from NLTK calculates the sentiment score.

## Technologies Used
- Python
- NLTK
- NumPy
- Pandas
- Matplotlib

## Project Structure

facebook-sentiment-analysis  
│  
├── sentiment_analysis.py  
├── kindle.txt  
├── requirements.txt  
└── README.md  

## How to Run the Project

### Install required libraries

pip install -r requirements.txt

### Run the program

python sentiment_analysis.py

## Dataset
The project uses a text file called `kindle.txt` which contains sample review sentences used for sentiment analysis.

## Output
The program processes the text and shows:
- Tokenized sentences and words
- Stemming results
- Lemmatization results
- POS tagging
- Sentiment score for each sentence

Example Output

Sentence: This product is amazing  
Scores: {'neg': 0.0, 'neu': 0.34, 'pos': 0.66, 'compound': 0.82}

## Conclusion
This project demonstrates how Natural Language Processing techniques can be used to analyze text data and identify sentiment in reviews or comments.
