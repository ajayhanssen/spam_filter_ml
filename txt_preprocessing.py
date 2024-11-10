import re

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

# change numbers to 'number'
def change_numbers(text):
    return re.sub(r'\b\d+\b', 'number', text)

if __name__ == '__main__':
    # load sample email
    file = open('./datasets/20021010_easy_ham/easy_ham/0001.ea7e79d3153e7469e7a9c3e0af6a357e', 'r')
    sample_email = file.read()
    print('\n#-#-#-#-#-#-#-#-#-Original-#-#-#-#-#-#-#-#-#-#-#-#\n\n', sample_email)

    sample_email = remove_html_tags(sample_email)
    print('\n#-#-#-#-#-#-#-#-#-Change HTML-#-#-#-#-#-#-#-#-#-#-#-#\n\n', sample_email)

    sample_email = change_email_addresses(sample_email)
    print('\n#-#-#-#-#-#-#-#-#-Change Email-#-#-#-#-#-#-#-#-#-#-#\n\n', sample_email)

    sample_email = change_http_urls(sample_email)
    print('\n#-#-#-#-#-#-#-#-#-Change URL-#-#-#-#-#-#-#-#-#-#-#\n\n', sample_email)

    #sample_email = change_numbers(sample_email)

    file.close()
    # save the preprocessed email
    file = open('processed_email.txt', 'w')
    file.write(sample_email)
    file.close()