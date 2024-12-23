from email import policy
from email.parser import BytesParser
from nltk.stem.snowball import SnowballStemmer
import re
from string import punctuation

################################################################################
# Not a huge fan of jupyter notebooks, so I tested the Preprocessing code here.#
#           There is nothing here that is not in the notebook                  #
#      (the jupyter notebook is also more commented than this file)            #
################################################################################

class EmailPreprocessor:
    def __init__(self):
        pass

    def extract_email_parts(self, file_path):
        with open(file_path, 'rb') as file:
            # Parse the email using the default policy
            email_message = BytesParser(policy=policy.default).parse(file)
        
        # Extract headers
        subject = email_message.get('Subject', '(No Subject)')
        sender = email_message.get('From', '(Unknown Sender)')
        recipient = email_message.get('To', '(Unknown Recipient)')
        
        # Extract body
        body = ""
        if email_message.get_body(preferencelist=('plain', 'html')):
            body_content = email_message.get_body(preferencelist=('plain', 'html'))
            body = body_content.get_content()  # Automatically decodes and gets the content
        
        return {
            "Subject": subject,
            "From": sender,
            "To": recipient,
            "Body": body.strip()
        }

    def stem_and_regex(self, email_dict):
        # create one string from the email parts
        email_string = email_dict["Subject"] + " " + email_dict["From"] + " " + email_dict["To"] + " " + email_dict["Body"]
        email_string = email_string.lower()

        # perform regex operations
        # change email adresses to 'emailaddr'
        email_string = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', 'emailaddr', email_string)

        # change urls to 'httpaddr'
        email_string = re.sub(r'(http|https)://[^\s]*', 'httpaddr', email_string)

        # change time to 'time'
        email_string = re.sub(r'\b\d{1,2}:\d{1,2}(:\d{1,2})?\b', 'time', email_string)

        # change date to 'date'
        email_string = re.sub(r'\b\d{1,2}/\d{1,2}/\d{4}\b', 'date', email_string)

        # change dollar to 'dollar'
        email_string = re.sub(r'\$\S+', 'dollar', email_string)

        # change www to 'wwwaddr'
        email_string = re.sub(r'\bwww\.[^\s]*\b', 'wwwaddr', email_string)

        # change percentages to 'percent'
        email_string = re.sub(r'\b\d+%', 'percent', email_string)

        # change ip to 'ipaddr'
        email_string = re.sub(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', 'ipaddr', email_string)

        # change numbers to 'number'
        email_string = re.sub(r'\b\d+\b', 'number', email_string)

        # Remove itemization prefixes (bullets, numbered lists, etc.)
        email_string = re.sub(r'^\s*[\d\w][\.\)\-]\s*|[\u2022\u2219\u25CB·]\s*', '', email_string, flags=re.MULTILINE)

        # other processing tasks
        # remove punctuation
        email_string = email_string.translate(str.maketrans('', '', punctuation))
        email_string = email_string.replace('\n', ' ')
        email_string = email_string.replace('\t', ' ')

        # remove multiple spaces
        email_string = re.sub(r'\s+', ' ', email_string)

        # stem the words
        stemmer = SnowballStemmer('english')
        email_string = ' '.join([stemmer.stem(word) for word in email_string.split()])

        return email_string

    def process_email(self,email_file_path):
        email_parts = self.extract_email_parts(email_file_path)
        processed = self.stem_and_regex(email_parts)

        return processed

# Example usage
if __name__ == '__main__':
    email_file_path = './datasets/20021010_spam/spam/0100.c60d1c697136b07c947fa180ba3e0441'
    processor = EmailPreprocessor()
    processed = processor.process_email(email_file_path)

    print(processed)

    