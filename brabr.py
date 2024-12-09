import re
from nltk.stem.snowball import SnowballStemmer
from string import punctuation
from email import message_from_string

def preprocess_text(email):
    pass

if __name__ == '__main__':
    file = open('./datasets/20021010_spam/spam/0486.348918a564335556b4fdd8b82f939918', 'r')
    sample_email = file.read()

    sample_email = message_from_string(sample_email)

    print(sample_email.get_payload())