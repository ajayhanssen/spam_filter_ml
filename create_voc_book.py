import os
from txt_preprocessing import *
from collections import Counter
import chardet

if __name__ == '__main__':
    # iterate through all files in the spam folder
    spam_dir = './datasets/20021010_spam/spam/'
    spam_files = os.listdir(spam_dir)

    mega_string = ''

    for file in spam_files:
        print(file)

        try:
            file_email = open(spam_dir + file, 'rb')
            raw_data = file_email.read(10000)  # Read a portion of the file
            result = chardet.detect(raw_data)
            encoding = result['encoding']
            file_email.close()


            file_email = open(spam_dir + file, 'r', encoding=encoding)
            email = file_email.read()
            email = process_email(email)
            mega_string += ' '.join(email) + ' '
            file_email.close()
        except:
            print('Error processing file: ' + file)
    
    word_count = Counter(mega_string)

    x = 100
    most_common_words = word_count.most_common(x)
    print(most_common_words)