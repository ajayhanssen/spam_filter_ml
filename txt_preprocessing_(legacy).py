import re
from nltk.stem.snowball import SnowballStemmer
from string import punctuation
from collections import Counter

################################################################################
#     Legacy preprocessing code, before knowing the email packages exists      #
#     This code still includes lots of html stuff and has been abandoned       #
################################################################################


# remove html tags
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# change email-adresses to 'emailaddr'
def change_email_addresses(text):
    return re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', 'emailaddr', text)

# change urls to 'httpaddr'
def change_http_urls(text):
    return re.sub(r'(http|https)://[^\s]*', 'httpaddr', text)

def change_time(text):
    return re.sub(r'\b\d{1,2}:\d{1,2}(:\d{1,2})?\b', 'time', text)

def change_date(text):
    return re.sub(r'\b\d{1,2}/\d{1,2}/\d{4}\b', 'date', text)

def change_ip(text):
    return re.sub(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', 'ipaddr', text)
    
def change_dollar(text):
    text = re.sub(r'\$\d+(\,\d+)?', 'dollar', text)
    return re.sub(r'\$\d+(\.\d+)?', 'dollar', text)

def change_www(text):
    return re.sub(r'\bwww\.[^\s]*\b', 'wwwaddr', text)

def change_numbers(text):
    return re.sub(r'\b\d+\b', 'number', text)

def change_percent(text):
    text = re.sub(r'\%\d+', 'percent', text)
    return re.sub(r'\b\d+\%\b', 'percent', text)

def replace_multiple_numbers(text):
    # change numbernumber+ to number
    return re.sub(r'(number)+', 'number', text)

def preprocess_text(text):
    text = remove_html_tags(text)
    text = change_email_addresses(text)
    text = change_http_urls(text)
    text = change_time(text)
    text = change_ip(text)
    text = change_dollar(text)
    text = change_percent(text)
    text = change_www(text)
    text = change_numbers(text)
    text = text.lower()
    return text

def process_email(email):
    email = preprocess_text(email)
    email = re.sub(r'\=', ' ', email)

    email = email.translate(str.maketrans('', '', punctuation))
    email = replace_multiple_numbers(email)
    email = email.replace('\n', ' ')
    email = email.replace('\t', ' ')
    email = re.sub(r'\ +', ' ', email)
    # remove words with more than 44 characters
    email = re.sub(r'\b\w{30,}\b', '', email)

    mega_string = ''

    email = email.split()
    for token in email:
        token = re.sub('[^a-zA-Z0-9]', '', token)
        stemmer = SnowballStemmer("english")
        token = stemmer.stem(token.strip())
        if len(token) < 1:
            continue
        mega_string += token + ' '
        #print(token)
    return mega_string.split()


if __name__ == '__main__':
    # load sample email
    #file = open('./datasets/20021010_easy_ham/easy_ham/0001.ea7e79d3153e7469e7a9c3e0af6a357e', 'r')
    file = open('./datasets/20021010_spam/spam/0100.c60d1c697136b07c947fa180ba3e0441', 'r')

    sample_email = file.read()
    print(sample_email)

    sample_email = process_email(sample_email)
    print(sample_email)

    """ file.close()
    # save the preprocessed email
    file = open('processed_email.txt', 'w')
    file.write(sample_email)
    file.close() """