###
# Module with functions that read data from a raw email
#
import re

# name of the file with the raw email
EMAIL_FILE = 'email.txt'

# Helper: returns the whole content of the email file
def read_email():
    with open(EMAIL_FILE, 'r', encoding='utf-8') as file:
        return file.read()

# Returns the sender email address (from the "From:" line)
def email_sender():
    # ^ with re.MULTILINE - start of any line
    # <(.+?)> - the address between < and >
    match = re.search(r'^From:.*<(.+?)>', read_email(), re.MULTILINE)
    return match.group(1)

# Returns the recipient email address (from the "To:" line)
def email_recipient():
    match = re.search(r'^To:.*<(.+?)>', read_email(), re.MULTILINE)
    return match.group(1)

# Returns the email subject (the rest of the "Subject:" line)
def email_subject():
    match = re.search(r'^Subject: (.*)$', read_email(), re.MULTILINE)
    return match.group(1)

# Returns the email body - everything after the first empty line
def email_body():
    # re.DOTALL - the dot also matches new lines, so (.*) takes the rest of the file
    match = re.search(r'\n\n(.*)', read_email(), re.DOTALL)
    return match.group(1).strip()