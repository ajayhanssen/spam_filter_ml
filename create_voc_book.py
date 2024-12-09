import os
from txt_preprocessing import *
from collections import Counter

if __name__ == '__main__':
    # iterate through all files in the spam folder
    spam_dir = './datasets/20021010_spam/spam/'
    spam_files = os.listdir(spam_dir)

    mega_string = ''
    for file in spam_files:
        file = open(spam_dir + file, 'r')
        email = file.read()
        email = process_email(email)
        mega_string += ' '.join(email) + ' '
        file.close()
    
    word_count = Counter(mega_string)

    x = 100
    most_common_words = word_count.most_common(x)
    print(most_common_words)