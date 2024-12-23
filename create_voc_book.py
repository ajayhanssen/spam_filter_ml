import os
from txt_preprocessing import *
from collections import Counter
import chardet

if __name__ == '__main__':
    # iterate through all files in the spam folder
    spam_dir = './datasets/20021010_spam/spam/'
    spam_files = os.listdir(spam_dir)

    mega_string_list = []
    not_readable = 0

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
            mega_string_list.extend(email)
            file_email.close()
        except:
            print('Error processing file: ' + file)
            not_readable += 1
    print(f'Number of files not readable: {not_readable}')
    print(f'Number of files successfully read: {len(spam_files) - not_readable}')

    #print(mega_string_list)
    #words = mega_string.split()
    #print(words)
    word_count = Counter(mega_string_list)

    x = 8791
    most_common_words = word_count.most_common(x)
    print(most_common_words)