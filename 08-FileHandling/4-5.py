###
# Prints data read from a raw email
#
import emails

def main():
    print('Sender:', emails.email_sender())
    print('Recipient:', emails.email_recipient())
    print('Subject:', emails.email_subject())
    print('Body:')
    print(emails.email_body())

if __name__ == "__main__":
    main()