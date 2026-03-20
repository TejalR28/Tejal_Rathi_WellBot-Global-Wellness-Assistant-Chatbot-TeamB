import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Sample text
text = "Indhu is studying Computer Science in India"

print("Original Text:")
print(text)

# Tokenization
tokens = word_tokenize(text)
print("\nTokens:")
print(tokens)